from __future__ import annotations

import secrets
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.constants.wishlist import WishlistLimits
from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin

if TYPE_CHECKING:
    from app.core.models import User


def generate_invite_token() -> str:
    return secrets.token_urlsafe(16)


class Wishlist(IntIdPkMixin, ObservableMixin, Base):
    title: Mapped[str] = mapped_column(String(WishlistLimits.TITLE_MAX))
    description: Mapped[str | None] = mapped_column(Text)
    invite_token: Mapped[str] = mapped_column(
        String(WishlistLimits.INVITE_TOKEN_MAX),
        unique=True,
        default=generate_invite_token,
    )

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    owner: Mapped[User] = relationship(back_populates="owned_wishlists")
