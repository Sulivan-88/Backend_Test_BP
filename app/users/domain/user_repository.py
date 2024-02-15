from abc import ABC, abstractmethod
from app.models.user_model import UserResponse
from app.users.infrastructure.users_table import User


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> UserResponse:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: int) -> UserResponse:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user_id: int, user: User) -> UserResponse:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError

    def get_all_users(self) -> UserResponse:
        raise NotImplementedError
