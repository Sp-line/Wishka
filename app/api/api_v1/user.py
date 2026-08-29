from fastapi import APIRouter

from app.core.auth.fastapi_users import fastapi_users
from app.core.config import settings
from app.schemas.user import UserRead
from app.schemas.user import UserUpdate

router = APIRouter(prefix=settings.api.v1.users)

router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
