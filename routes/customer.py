from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.errors import DuplicateKeyError
from utils.mongo import get_customers_collection
from utils.auth import verify_token
from schema.customer_schema import ToggleVerificationRequest, CustomersListResponse
from models.customer import Customer
from datetime import datetime

router = APIRouter()


@router.get("/users", response_model=list[Customer])
async def get_all_users(token: str = Depends(verify_token)):

    customer_collection = get_customers_collection()

    users = customer_collection.find()

    users_list = [Customer.from_mongo(user) for user in users] 
    
    return users_list

@router.put("/toggle-verification", response_model=Customer)
async def toggle_user_verification(request: ToggleVerificationRequest, token: str = Depends(verify_token)):

    customer_collection = get_customers_collection()

    user = customer_collection.find_one({"email": request.email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_verification_status = not user['isVerified']  # Invert the current status

    updated_user = customer_collection.find_one_and_update(
        {"email": request.email},
        {"$set": {"isVerified": new_verification_status, "updatedAt": datetime.utcnow()}},
        return_document=True  # Return the updated document
    )

    return Customer(**updated_user)
