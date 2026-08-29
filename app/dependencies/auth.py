from collections.abc import AsyncIterator  # noqa: TC003
from typing import Annotated

from dishka.integrations.fastapi import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002

from app.core.auth.user_database import ErrorHandlingUserDatabase
from app.core.auth.user_manager import UserManager
from app.core.models.oauth_account import OAuthAccount
from app.core.models.user import User
from app.core.types.user import UserID  # noqa: TC001


@inject
async def get_user_db(
    session: FromDishka[AsyncSession],
) -> AsyncIterator[ErrorHandlingUserDatabase[User, UserID]]:
    yield ErrorHandlingUserDatabase(
        session=session,
        user_table=User,
        oauth_account_table=OAuthAccount,
    )


async def get_user_manager(
    user_db: Annotated[ErrorHandlingUserDatabase[User, UserID], Depends(get_user_db)],
) -> AsyncIterator[UserManager]:
    yield UserManager(user_db=user_db)
