from typing import Annotated

from fastapi_users.schemas import BaseUser
from fastapi_users.schemas import BaseUserCreate
from fastapi_users.schemas import BaseUserUpdate
from pydantic import HttpUrl
from pydantic import UrlConstraints

from app.constants.user import UserLimits
from app.core.types.user import UserID

type UserPhotoUrl = Annotated[
    HttpUrl,
    UrlConstraints(
        max_length=UserLimits.PHOTO_URL_MAX,
        allowed_schemes=["http", "https"],
    ),
]


class UserCreate(BaseUserCreate): ...


class UserUpdate(BaseUserUpdate): ...


class UserRead(BaseUser[UserID]):
    photo_url: UserPhotoUrl | None = None
