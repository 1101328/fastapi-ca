from dependency_injector.wiring import inject, Provide
from app.containers import Container
from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str

@router.post("")
@inject
def create_user(
    user: CreateUserBody,
    user_service: UserService = Depends(Provide[Container.user_service]),
    ):
    created_user = user_service.create_user(
        name =user.name, 
        email = user.email, 
        password = user.password
        )

    return created_user