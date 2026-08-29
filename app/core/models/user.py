from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.constants.user import UserLimits
from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin
from app.core.types.user import UserID

if TYPE_CHECKING:
    from app.core.models.gift import Gift
    from app.core.models.oauth_account import OAuthAccount
    from app.core.models.reservation import Reservation
    from app.core.models.wishlist import Wishlist
    from app.core.models.wishlist_members import WishlistMember


class User(Base, IntIdPkMixin, ObservableMixin, SQLAlchemyBaseUserTable[UserID]):
    photo_url: Mapped[str | None] = mapped_column(String(UserLimits.PHOTO_URL_MAX))
    username: Mapped[str | None] = mapped_column(String(UserLimits.USERNAME_MAX))

    oauth_accounts: Mapped[list[OAuthAccount]] = relationship(lazy="joined")

    owned_wishlists: Mapped[list[Wishlist]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    reservations: Mapped[list[Reservation]] = relationship(
        back_populates="reserver",
        cascade="all, delete-orphan",
    )
    wishlist_member_associations: Mapped[list[WishlistMember]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    reserved_gifts: Mapped[list[Gift]] = relationship(
        secondary="reservations",
        back_populates="reservers",
        viewonly=True,
        overlaps="reservations",
    )
    member_wishlists: Mapped[list[Wishlist]] = relationship(
        secondary="wishlist_members",
        back_populates="users",
        viewonly=True,
        overlaps="wishlist_member_associations",
    )
