from typing import Annotated

from annotated_types import MaxLen
from annotated_types import MinLen
from fastapi_users.schemas import BaseUser
from fastapi_users.schemas import BaseUserCreate
from fastapi_users.schemas import BaseUserUpdate
from pydantic import AfterValidator
from pydantic import HttpUrl
from pydantic import StringConstraints

from app.constants.user import UserLimits
from app.core.types.user import UserID
from app.schemas.validators.username import validate_username_characters
from app.schemas.validators.username import validate_username_consecutive_symbols
from app.schemas.validators.username import validate_username_not_all_digits
from app.schemas.validators.username import validate_username_start_finish

type UserAvatarS3Key = Annotated[
    str,
    MinLen(UserLimits.AVATAR_S3_KEY_MIN),
    MaxLen(UserLimits.AVATAR_S3_KEY_MAX),
]
type Username = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        to_lower=True,
        min_length=UserLimits.USERNAME_MIN,
        max_length=UserLimits.USERNAME_MAX,
    ),
    AfterValidator(validate_username_characters),
    AfterValidator(validate_username_start_finish),
    AfterValidator(validate_username_consecutive_symbols),
    AfterValidator(validate_username_not_all_digits),
]


class UserCreate(BaseUserCreate):
    username: Username | None = None


class UserCreateDB(UserCreate):
    avatar_s3_key: UserAvatarS3Key | None = None


class UserUpdate(BaseUserUpdate):
    username: Username | None = None


class UserUpdateDB(UserUpdate):
    avatar_s3_key: UserAvatarS3Key | None = None


class UserRead(BaseUser[UserID]):
    avatar_url: HttpUrl | None = None
    username: str | None = None
