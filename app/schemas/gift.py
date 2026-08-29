from decimal import Decimal
from typing import Annotated

from annotated_types import Ge
from annotated_types import Le
from annotated_types import MaxLen
from annotated_types import MinLen
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import HttpUrl
from pydantic import PositiveInt
from pydantic import UrlConstraints

from app.constants.gift import Currency
from app.constants.gift import GiftLimits
from app.schemas.base import Id

type GiftTitle = Annotated[
    str,
    MinLen(GiftLimits.TITLE_MIN),
    MaxLen(GiftLimits.TITLE_MAX),
]
type GiftPriority = Annotated[
    int,
    Ge(GiftLimits.PRIORITY_MIN),
    Le(GiftLimits.PRIORITY_MAX),
]
type GiftQuantity = Annotated[
    int,
    Ge(GiftLimits.QUANTITY_MIN),
]
type GiftPrice = Annotated[
    Decimal,
    Ge(GiftLimits.PRICE_MIN),
]
type GiftUrl = Annotated[
    HttpUrl,
    UrlConstraints(
        max_length=GiftLimits.URL_MAX,
        allowed_schemes=["http", "https"],
    ),
]
type GiftImageUrl = Annotated[
    HttpUrl,
    UrlConstraints(
        max_length=GiftLimits.IMAGE_URL_MAX,
        allowed_schemes=["http", "https"],
    ),
]
type GiftNote = Annotated[
    str,
    MinLen(GiftLimits.NOTE_MIN),
    MaxLen(GiftLimits.NOTE_MAX),
]


class GiftBase(BaseModel):
    title: GiftTitle
    priority: GiftPriority
    quantity: GiftQuantity = GiftLimits.QUANTITY_DEFAULT
    price: GiftPrice | None = GiftLimits.PRICE_DEFAULT
    currency: Currency | None = None
    url: GiftUrl | None = None
    note: GiftNote | None = None


class GiftBaseWithRelation(GiftBase):
    wishlist_id: PositiveInt


class GiftCreateReq(GiftBaseWithRelation): ...


class GiftCreateDB(GiftBaseWithRelation):
    image_url: GiftImageUrl | None = None


class GiftUpdateReq(BaseModel):
    title: GiftTitle | None = None
    priority: GiftPriority | None = None
    quantity: GiftQuantity | None = None
    price: GiftPrice | None = None
    currency: Currency | None = None
    url: GiftUrl | None = None
    note: GiftNote | None = None


class GiftUpdateDB(BaseModel):
    title: GiftTitle | None = None
    priority: GiftPriority | None = None
    quantity: GiftQuantity | None = None
    price: GiftPrice | None = None
    currency: Currency | None = None
    url: GiftUrl | None = None
    image_url: GiftImageUrl | None = None
    note: GiftNote | None = None
    wishlist_id: PositiveInt | None = None


class GiftRead(Id, GiftBaseWithRelation):
    image_url: GiftImageUrl | None = None

    model_config = ConfigDict(from_attributes=True)
