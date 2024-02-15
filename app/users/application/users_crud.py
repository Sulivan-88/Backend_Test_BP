from fastapi import HTTPException

from app.models.user_model import UserCreate, UserResponse, RoleResponse
from app.shared.external_api import get_info
from app.users.domain.user_repository import UserRepository
from app.users.infrastructure.users_table import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> UserResponse:
        return self.user_repository.create_user(user)

    def get_user(self, user_id: int) -> UserResponse:
        return self.user_repository.get_user(user_id)

    def update_user(self, user_id: int, user: User) -> UserResponse:
        return self.user_repository.update_user(user_id, user)

    def delete_user(self, user_id: int) -> None:
        return self.user_repository.delete_user(user_id)

    def get_all_users(self) -> UserResponse:
        return self.user_repository.get_all_users()

    def get_info_by_role(self, user_id: int) -> str:
        role = self.user_repository.get_info_by_role(user_id)
        if not role:
            raise HTTPException(status_code=404, detail="User not found")
        return get_info(role)
