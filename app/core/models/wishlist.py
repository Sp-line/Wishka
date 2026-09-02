from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean
from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.constants.wishlist import WishlistLimits
from app.constants.wishlist import WishlistPrivacy
from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin

if TYPE_CHECKING:
    from app.core.models.gift import Gift
    from app.core.models.user import User
    from app.core.models.wishlist_member import WishlistMember


class Wishlist(IntIdPkMixin, ObservableMixin, Base):
    title: Mapped[str] = mapped_column(String(WishlistLimits.TITLE_MAX))
    description: Mapped[str | None] = mapped_column(
        String(WishlistLimits.DESCRIPTION_MAX),
    )
    privacy: Mapped[WishlistPrivacy] = mapped_column(
        SAEnum(
            WishlistPrivacy,
            native_enum=False,
            length=WishlistLimits.PRIVACY_MAX,
            values_callable=lambda obj: [e.value for e in obj],
        ),
        default=WishlistPrivacy.PUBLIC,
    )
    is_reservable: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default="true",
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    owner: Mapped[User] = relationship(back_populates="owned_wishlists")

    gifts: Mapped[list[Gift]] = relationship(
        back_populates="wishlist",
        cascade="all, delete-orphan",
    )
    wishlist_member_associations: Mapped[list[WishlistMember]] = relationship(
        back_populates="wishlist",
        cascade="all, delete-orphan",
    )

    users: Mapped[list[User]] = relationship(
        secondary="wishlist_members",
        back_populates="member_wishlists",
        viewonly=True,
        overlaps="wishlist_member_associations",
    )
