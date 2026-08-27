from typing import TYPE_CHECKING

from dishka.integrations.fastapi import FromDishka  # noqa: TC002
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002

from app.core.models.oauth_account import OAuthAccount
from app.core.models.user import User

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from app.core.types.user import UserID


async def get_user_db(
    session: FromDishka[AsyncSession],
) -> AsyncIterator[SQLAlchemyUserDatabase[User, UserID]]:
    yield SQLAlchemyUserDatabase(
        session=session,
        user_table=User,
        oauth_account_table=OAuthAccount,
    )
