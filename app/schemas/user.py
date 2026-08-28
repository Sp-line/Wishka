from fastapi_users.schemas import BaseUser
from fastapi_users.schemas import BaseUserCreate
from fastapi_users.schemas import BaseUserUpdate

from app.core.types.user import UserID


class UserCreate(BaseUserCreate): ...


class UserUpdate(BaseUserUpdate): ...


class UserRead(BaseUser[UserID]): ...
