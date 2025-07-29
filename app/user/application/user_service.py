from typing import Annotated
from dependency_injector.wiring import inject
import ulid
from datetime import datetime
from fastapi import HTTPException, Depends
from app.user.domain.user import User
from app.user.domain.repository.user_repo import IUserRepository
from app.user.infra.repository.user_repo import UserRepository
from app.utils.crypto import Crypto

class UserService:
    @inject
    def __init__(
        self,
        user_repo: IUserRepository,
    ):
        self.user_repo = user_repo

    def create_user(
            self,
            name:str,
            email:str,
            password:str,
            memo: str | None = None,
            ):
        _user = None

        try:
            _user = self.user_repo.find_by_email(email)
        except Exception as e:
            if e.status_code != 400:
                raise e

        if _user:
            raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다")

        now = datetime.now()
        user: User = User(
            id=str(ulid.new()),
            name=name,
            email=email,
            password=self.crypto.encrypt(password),
            memo=memo,
            created_at=now,
            updated_at=now
        )
        self.user_repo.save(user)

        return user