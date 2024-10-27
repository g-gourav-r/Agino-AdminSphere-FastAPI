from fastapi import APIRouter, HTTPException, Request
from controllers.admin_controller import AdminController

router = APIRouter()
admin_controller = AdminController()

@router.post("/admin/register")
async def register_admin(request: Request):
    """Register a new admin account."""
    data = await request.json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    
    if not username or not email or not password:
        raise HTTPException(status_code=400, detail="All fields are required.")
    
    result = admin_controller.register_admin(username, email, password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result

@router.post("/admin/login")
async def login_admin(request: Request):
    """Log in an admin and return a JWT token."""
    data = await request.json()
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        raise HTTPException(status_code=400, detail="Both email and password are required.")
    
    result = admin_controller.login_admin(email, password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return result
