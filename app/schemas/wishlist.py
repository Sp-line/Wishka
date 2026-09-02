from typing import Annotated

from annotated_types import MaxLen
from annotated_types import MinLen
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PositiveInt

from app.constants.wishlist import WishlistLimits
from app.constants.wishlist import WishlistPrivacy
from app.core.models.wishlist import generate_invite_token
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
type WishlistInviteToken = Annotated[
    str,
    MinLen(WishlistLimits.INVITE_TOKEN_MIN),
    MaxLen(WishlistLimits.INVITE_TOKEN_MAX),
]


class WishlistBase(BaseModel):
    title: WishlistTitle
    privacy: WishlistPrivacy = WishlistPrivacy.PUBLIC
    is_reservable: bool = True
    description: WishlistDescription | None = None


class WishlistCreateReq(WishlistBase): ...


class WishlistCreateDB(WishlistBase):
    owner_id: PositiveInt
    invite_token: WishlistInviteToken = Field(default_factory=generate_invite_token)


class WishlistUpdateBase(BaseModel):
    title: WishlistTitle | None = None
    privacy: WishlistPrivacy | None = None
    is_reservable: bool | None = None
    description: WishlistDescription | None = None


class WishlistUpdateReq(WishlistUpdateBase): ...


class WishlistUpdateDB(WishlistUpdateBase):
    invite_token: WishlistInviteToken | None = None

    owner_id: PositiveInt | None = None


class WishlistRead(Id, WishlistBase):
    invite_token: WishlistInviteToken
    owner_id: PositiveInt

    model_config = ConfigDict(from_attributes=True)
