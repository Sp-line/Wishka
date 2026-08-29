from __future__ import annotations

import secrets
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.constants.wishlist import WishlistLimits
from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin

if TYPE_CHECKING:
    from app.core.models.gift import Gift
    from app.core.models.user import User
    from app.core.models.wishlist_members import WishlistMember


def generate_invite_token() -> str:
    return secrets.token_urlsafe(16)


class Wishlist(IntIdPkMixin, ObservableMixin, Base):
    title: Mapped[str] = mapped_column(String(WishlistLimits.TITLE_MAX))
    description: Mapped[str | None] = mapped_column(
        String(WishlistLimits.DESCRIPTION_MAX),
    )
    invite_token: Mapped[str] = mapped_column(
        String(WishlistLimits.INVITE_TOKEN_MAX),
        unique=True,
        default=generate_invite_token,
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
