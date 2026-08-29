from __future__ import annotations

from decimal import Decimal  # noqa: TC003
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import SmallInteger
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.constants.gift import GiftLimits
from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin

if TYPE_CHECKING:
    from app.core.models import Wishlist


class Gift(IntIdPkMixin, ObservableMixin, Base):
    title: Mapped[str] = mapped_column(String(GiftLimits.TITLE_MAX))
    priority: Mapped[int] = mapped_column(SmallInteger)
    quantity: Mapped[int] = mapped_column(
        Integer,
        default=GiftLimits.QUANTITY_DEFAULT,
        server_default=str(GiftLimits.QUANTITY_DEFAULT),
    )
    price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))
    url: Mapped[str | None] = mapped_column(String(GiftLimits.URL_MAX))
    image_url: Mapped[str | None] = mapped_column(String(GiftLimits.IMAGE_URL_MAX))
    note: Mapped[str | None] = mapped_column(Text)

    wishlist_id: Mapped[int] = mapped_column(
        ForeignKey("wishlists.id", ondelete="CASCADE"),
        index=True,
    )

    wishlist: Mapped[Wishlist] = relationship(back_populates="gifts")
