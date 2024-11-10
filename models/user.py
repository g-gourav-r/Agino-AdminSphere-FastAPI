from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    created_at: datetime = datetime.utcnow()
    hashed_password: str
