from fastapi import APIRouter, Depends, HTTPException
from app.models.user_model import User
from app.users.application.users_crud import UserService
from app.users.infrastructure.users_sqlachemy_repository import SQLAlchemyUserRepository

router = APIRouter()
user_service = UserService(SQLAlchemyUserRepository())

@router.post("/users/")
async def create_user(user: User) -> User:
    return user_service.create_user(user)

@router.get("/users/{user_id}")
async def get_user(user_id: int) -> User:
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    return user_service.update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int) -> None:
    user_service.delete_user(user_id)
