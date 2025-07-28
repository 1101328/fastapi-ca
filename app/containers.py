from dependency_injector import containers, providers
from app.user.application.user_service import UserService

from app.user.infra.repository.user_repo import UserRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.user.interface.controllers"]
    )

    user_repo = providers.Singleton(UserRepository)
    user_service = providers.Factory(UserService, user_repo=user_repo)