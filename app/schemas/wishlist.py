from typing import Annotated

from annotated_types import MaxLen
from annotated_types import MinLen
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt

from app.constants.wishlist import WishlistLimits
from app.constants.wishlist import WishlistPrivacy
from app.schemas.base import Id

type WishlistTitle = Annotated[
    str,
    MinLen(WishlistLimits.TITLE_MIN),
    MaxLen(WishlistLimits.TITLE_MAX),
]
type WishlistDescription = Annotated[
    str,
    MinLen(WishlistLimits.DESCRIPTION_MIN),
    MaxLen(WishlistLimits.DESCRIPTION_MAX),
]


class WishlistBase(BaseModel):
    title: WishlistTitle
    privacy: WishlistPrivacy = WishlistPrivacy.PUBLIC
    is_reservable: bool = True
    description: WishlistDescription | None = None


class WishlistCreateReq(WishlistBase): ...


class WishlistCreateDB(WishlistBase):
    owner_id: PositiveInt


class WishlistUpdateBase(BaseModel):
    title: WishlistTitle | None = None
    privacy: WishlistPrivacy | None = None
    is_reservable: bool | None = None
    description: WishlistDescription | None = None


class WishlistUpdateReq(WishlistUpdateBase): ...


class WishlistUpdateDB(WishlistUpdateBase):
    owner_id: PositiveInt | None = None


class WishlistRead(Id, WishlistBase):
    owner_id: PositiveInt

    model_config = ConfigDict(from_attributes=True)
