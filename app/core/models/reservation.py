from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.constants.reservation import ReservationLimits
from app.core.models.base import Base
from app.core.models.mixins import IntIdPkMixin
from app.core.models.mixins import ObservableMixin

if TYPE_CHECKING:
    from app.core.models import Gift
    from app.core.models import User


class Reservation(IntIdPkMixin, ObservableMixin, Base):
    __tablename__ = "reservations"

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=ReservationLimits.QUANTITY_DEFAULT,
        server_default=str(ReservationLimits.QUANTITY_DEFAULT),
    )

    gift_id: Mapped[int] = mapped_column(
        ForeignKey("gifts.id", ondelete="CASCADE"),
        index=True,
    )
    reserver_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    gift: Mapped[Gift] = relationship(back_populates="reservations")
    reserver: Mapped[User] = relationship(back_populates="reservations")

    __table_args__ = (
        UniqueConstraint(
            "gift_id",
            "reserver_id",
            name="uq_reservations_gift_id_reserver_id",
        ),
    )
