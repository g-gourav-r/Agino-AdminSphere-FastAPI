from fastapi import Depends, HTTPException, status
from utils.jwt_handler import verify_access_token
from models.user_model import UserModel

user_model = UserModel()

def get_all_users(token: str = Depends(verify_access_token)):
    """Return all users if the JWT token is valid."""
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or expired",
        )
    
    users = user_model.get_all_users()
    return {"users": users}
