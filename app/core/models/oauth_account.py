from fastapi_users_db_sqlalchemy import SQLAlchemyBaseOAuthAccountTable
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.types.user import UserID


class OAuthAccount(Base, IntIdPkMixin, SQLAlchemyBaseOAuthAccountTable[UserID]):
    user_id: Mapped[UserID] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
    )
