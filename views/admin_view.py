from fastapi import APIRouter, HTTPException
from controllers.admin_controller import AdminController

router = APIRouter()
admin_controller = AdminController()

@router.post("/admin/register")
async def register_admin(username: str, email: str, password: str):
    """Register a new admin account."""
    result = admin_controller.register_admin(username, email, password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.post("/admin/login")
async def login_admin(email: str, password: str):
    """Log in an admin and return a JWT token."""
    result = admin_controller.login_admin(email, password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
