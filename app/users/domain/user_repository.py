from abc import ABC, abstractmethod
from app.models.user_model import User


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass