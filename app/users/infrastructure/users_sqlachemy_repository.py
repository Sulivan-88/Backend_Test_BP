from sqlalchemy.orm import Session
from app.users.domain.user_repository import UserRepository
from app.models.user_model import User
from app.shared.base import SessionLocal


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session = SessionLocal()):
        self.session = session

    def create_user(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id: int, user: User) -> User:
        db_user = self.get_user(user_id)
        db_user.username = user.username
        db_user.email = user.email
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> None:
        self.session.query(User).filter(User.id == user_id).delete()
        self.session.commit()
