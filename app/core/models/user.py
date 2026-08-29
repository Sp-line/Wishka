from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin
from app.core.types.user import UserID

if TYPE_CHECKING:
    from app.core.models.oauth_account import OAuthAccount
    from app.core.models.wishlist import Wishlist


class User(Base, IntIdPkMixin, ObservableMixin, SQLAlchemyBaseUserTable[UserID]):
    oauth_accounts: Mapped[list[OAuthAccount]] = relationship(lazy="joined")

    owned_wishlists: Mapped[list[Wishlist]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
