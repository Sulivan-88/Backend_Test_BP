from app.models.user_model import UserCreate, UserResponse
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
        self.user_repository.delete_user(user_id)

    def get_all_users(self) -> UserResponse:
        return self.user_repository.get_all_users()
