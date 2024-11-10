from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from pymongo.errors import DuplicateKeyError
from utils.mongo import get_admin_collection
from utils.auth import create_access_token
from schema.user_schema import UserCreate, UserResponse
from models.user import User
from datetime import datetime
import re

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    # Accessing MongoDB collection
    admin_collection = get_admin_collection()

    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Convert user data to dictionary
    user_data = user.dict()
    
    # Check if essential fields are provided
    if not (user_data["username"] and user_data["first_name"] and user_data["last_name"] and user_data["email"] and user_data["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="All fields (username, first_name, last_name, email, password) are required."
        )

    # Check if email is in valid format
    if not is_valid_email(user_data["email"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format. Please provide a valid email."
        )

    # Hash the password and add it to the user data dictionary
    user_data["hashed_password"] = hashed_password
    user_data.pop("password")  # Remove the plain password from the user data

    # Add created_at field
    user_data["created_at"] = datetime.utcnow()

    try:
        # Attempt to insert the user data into the database
        admin_collection.insert_one(user_data)
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already registered.")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {str(e)}")

    # Return the UserResponse model after successful signup
    return UserResponse(**user_data)

@router.post("/login")
async def login(username: str, password: str):
    admin_collection = get_admin_collection()
    user = admin_collection.find_one({"username": username})
    
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
