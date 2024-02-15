from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapper

from app.shared.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    role = Column(String)
