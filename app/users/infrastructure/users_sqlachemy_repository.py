from typing import Dict, Any

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from app.users.domain.user_repository import UserRepository
from app.shared.base import SessionLocal
from app.users.infrastructure.users_table import User


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session = SessionLocal()):
        self.session = session

    def create_user(self, user: User) -> User:
        create_user = User(id=user.id, name=user.name, description=user.description, role=user.role)
        self.session.add(create_user)
        self.session.commit()
        self.session.refresh(create_user)
        return create_user

    def get_user(self, user_id: int) -> User:
        query = select(User).where(User.id == user_id)
        user = self.session.execute(query)
        return user.scalar_one_or_none()

    def update_user(self, user_id: int, user: User) -> User:
        db_user = self.get_user(user_id)
        db_user.name = user.name
        db_user.description = user.description
        db_user.role = user.role
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> None:
        self.session.query(User).filter(User.id == user_id).delete()
        self.session.commit()

    def get_all_users(self) -> list[User]:
        return self.session.query(User).all()

    def get_info_by_role(self, user_id: int) -> dict[str, Result] | dict[Any, Any]:
        query = select(User.role).where(User.id == user_id)
        role = self.session.execute(query)
        return role.scalar_one_or_none()
