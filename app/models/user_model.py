from typing import Optional
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    role: Optional[str] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    role: Optional[str] = None


class UserCreate(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    role: Optional[str] = None


class RoleResponse(BaseModel):
    role: Optional[str] = None

