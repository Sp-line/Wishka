from typing import TYPE_CHECKING

from fastapi_users.authentication import JWTStrategy

from app.core.config import settings

if TYPE_CHECKING:
    from app.core.models.user import User
    from app.core.types.user import UserID


def get_jwt_strategy() -> JWTStrategy[User, UserID]:
    return JWTStrategy(
        secret=settings.auth.secret,
        lifetime_seconds=settings.auth.lifetime_seconds,
    )
