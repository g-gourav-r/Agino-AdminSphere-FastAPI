from fastapi import APIRouter, Depends
from controllers.user_controller import get_all_users

router = APIRouter()

@router.get("/api/admin/users", response_model=dict)
async def read_users(token: str = Depends(get_all_users)):
    return token