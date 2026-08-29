from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin

if TYPE_CHECKING:
    from app.core.models import User
    from app.core.models import Wishlist


class WishlistMember(IntIdPkMixin, ObservableMixin, Base):
    __tablename__ = "wishlist_members"

    wishlist_id: Mapped[int] = mapped_column(
        ForeignKey("wishlists.id", ondelete="CASCADE"),
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    wishlist: Mapped[Wishlist] = relationship(
        back_populates="wishlist_member_associations",
    )
    user: Mapped[User] = relationship(back_populates="wishlist_member_associations")

    __table_args__ = (
        UniqueConstraint(
            "wishlist_id",
            "user_id",
            name="uq_wishlist_members_wishlist_id_user_id",
        ),
    )
