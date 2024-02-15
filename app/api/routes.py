from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.models.user_model import UserUpdate, UserCreate, UserResponse
from app.users.application.users_crud import UserService
from app.users.infrastructure.users_sqlachemy_repository import SQLAlchemyUserRepository

router = APIRouter()
user_service = UserService(SQLAlchemyUserRepository())



@router.get(
    "/users/",
    status_code=status.HTTP_200_OK,
    response_model=List[UserResponse],
    summary="Obtiene una lista de todos los usuarios")
def get_all_users() -> UserResponse:
    try:
        return user_service.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
    summary="Obtiene un usuario con base en su id")
def get_user(user_id: int) -> UserResponse:
    try:
        user = user_service.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    summary="Crea un nuevo usuario")
def create_user(user: UserCreate) -> UserResponse:
    try:
        return user_service.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.patch("/users/{user_id}", summary="Actualiza los datos de un usuario con base en su id")
def update_user(user_id: int, user: UserUpdate) -> UserResponse:
    try:
        return user_service.update_user(user_id, user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Elimina un usuario")
def delete_user(user_id: int) -> Dict[str, str]:
    try:
        user_service.delete_user(user_id)
        return {"message": f"El usuario {user_id} ha sido borrado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get(
    "/roles_by_id/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
    summary="Obtiene informacion de acuerdo al rol del id del usuario")
def get_user(user_id: int) -> UserResponse:
    try:
        user = user_service.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
