from typing import Annotated

from annotated_types import Ge
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt

from app.constants.reservation import ReservationLimits
from app.schemas.base import Id

type ReservationQuantity = Annotated[
    int,
    Ge(ReservationLimits.QUANTITY_MIN),
]


class ReservationBase(BaseModel):
    quantity: ReservationQuantity = ReservationLimits.QUANTITY_DEFAULT


class ReservationBaseWithRelation(ReservationBase):
    gift_id: PositiveInt


class ReservationCreateReq(ReservationBaseWithRelation): ...


class ReservationCreateDB(ReservationBaseWithRelation):
    reserver_id: PositiveInt


class ReservationUpdateReq(BaseModel):
    quantity: ReservationQuantity | None = None


class ReservationUpdateDB(BaseModel):
    quantity: ReservationQuantity | None = None
    gift_id: PositiveInt | None = None
    reserver_id: PositiveInt | None = None


class ReservationRead(Id, ReservationBaseWithRelation):
    reserver_id: PositiveInt

    model_config = ConfigDict(from_attributes=True)
