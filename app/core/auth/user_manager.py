from typing import TYPE_CHECKING

from fastapi_users import BaseUserManager
from fastapi_users import IntegerIDMixin

from app.core.config import settings
from app.core.models.user import User
from app.core.types.user import UserID
from app.tasks.mail import send_reset_password_email_task
from app.tasks.mail import send_verification_email_task

if TYPE_CHECKING:
    from fastapi import Request


class UserManager(IntegerIDMixin, BaseUserManager[User, UserID]):
    reset_password_token_secret = (
        settings.auth.reset_password_token_secret.get_secret_value()
    )
    verification_token_secret = (
        settings.auth.verification_token_secret.get_secret_value()
    )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        _request: Request | None = None,
    ) -> None:
        link = str(settings.auth.verification_link).format(token=token)
        await send_verification_email_task.kiq(  # type: ignore[call-overload]
            email_to=user.email,
            verification_link=link,
        )

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        _request: Request | None = None,
    ) -> None:
        link = str(settings.auth.reset_link).format(token=token)
        await send_reset_password_email_task.kiq(  # type: ignore[call-overload]
            email_to=user.email,
            reset_link=link,
        )
