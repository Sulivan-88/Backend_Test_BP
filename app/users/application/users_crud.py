from app.users.domain.user_repository import UserRepository
from app.models.user_model import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        return self.user_repository.create_user(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user(user_id)

    def update_user(self, user_id: int, user: User) -> User:
        return self.user_repository.update_user(user_id, user)

    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete_user(user_id)
