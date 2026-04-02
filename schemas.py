from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel, Field


#  USER SCHEMAS

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: str
    role: str



class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    status: str

    class Config:
        from_attributes = True   # for SQLAlchemy


# RECORD SCHEMAS

class RecordCreate(BaseModel):
    amount: float = Field(..., gt=0)  #  must be > 0
    type: str
    category: str
    date: str
    note: Optional[str] = None
    user_id: int


class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: str
    note: Optional[str]
    user_id: int

    class Config:
        from_attributes = True