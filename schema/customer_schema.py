from pydantic import BaseModel, EmailStr
from datetime import datetime
from models.customer import Customer

class CustomersListResponse(BaseModel):
    customers: list[Customer]  

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class ToggleVerificationRequest(BaseModel):
    email: EmailStr