from abc import ABCMeta, abstractmethod
from app.user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> User:
        
        """
        이메일로 유저를 검색한다.
        검색한 유저가 없을 경우 400 에러를 발생시킨다.
        """
        raise NotImplementedError