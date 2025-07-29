from app.database import SessionLocal
from app.utils.db_utils import row_to_dict
from fastapi import HTTPException
from app.user.domain.user import User as UserVO
from app.user.infra.db_models.user import User
from app.user.domain.repository.user_repo import IUserRepository

class UserRepository(IUserRepository):
    def save(self, user: UserVO):
        new_user = User(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            memo=user.memo,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

        with SessionLocal() as db:
            try:
                db = SessionLocal()
                db.add(new_user)
                db.commit()
            finally:
                db.close()

    def find_by_email(self, email: str) -> UserVO:
        with SessionLocal() as db:
            
                user = db.query(User).filter(User.email == email).first()

                if not user:
                    raise HTTPException(status_code=400, detail="사용자를 찾을 수 없습니다")
                    
                return UserVO(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                )
          
          