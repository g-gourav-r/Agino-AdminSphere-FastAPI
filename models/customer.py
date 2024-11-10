from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from bson import ObjectId  # Importing ObjectId to handle MongoDB ObjectId

class Customer(BaseModel):
    id: str
    username: str
    email: str
    password: Optional[str] = None
    llmModel: Optional[str] = None
    createdAt: Optional[datetime] = None  # Keep datetime for internal use
    updatedAt: Optional[datetime] = None  # Keep datetime for internal use
    isVerified: bool
    isPrivilegedUser: Optional[bool] = False

    @classmethod
    def from_mongo(cls, data):
        # Handle _id field from MongoDB and convert to 'id'
        if "_id" in data:
            data["id"] = str(data["_id"])  # MongoDB ObjectId to string
            del data["_id"]  # Remove '_id' from the data dictionary
        
        # Ensure 'createdAt' and 'updatedAt' are strings formatted if datetime
        if isinstance(data.get("createdAt"), datetime):
            data["createdAt"] = data["createdAt"].isoformat()  # Convert datetime to ISO format string
        if isinstance(data.get("updatedAt"), datetime):
            data["updatedAt"] = data["updatedAt"].isoformat()  # Convert datetime to ISO format string

        # Return the Customer model with all the required transformations
        # Ensure id is present
        if "id" not in data:
            raise ValueError("id field is required")

        # Return the Customer model with all the required transformations
        return cls(**data)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else str(v)  # Automatically handle datetime serialization
        }


class ToggleVerificationResponse(BaseModel):
    email: str
    isVerified: bool
    updatedAt: datetime