from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime
