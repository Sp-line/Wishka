from datetime import datetime  # noqa: TC003
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt

from app.constants.token import TokenType


class JWTPayloadBase(BaseModel):
    sub: str | None = None
    exp: datetime | None = None
    type: TokenType


class WishlistInviteJWTPayload(JWTPayloadBase):
    type: Literal[TokenType.WISHLIST_INVITE] = TokenType.WISHLIST_INVITE
    wishlist_id: PositiveInt

    model_config = ConfigDict(from_attributes=True)
