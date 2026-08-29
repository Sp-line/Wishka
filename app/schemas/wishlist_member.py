from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PositiveInt

from app.schemas.base import Id


class WishlistMemberBase(BaseModel):
    wishlist_id: PositiveInt
    user_id: PositiveInt


class WishlistMemberCreateDB(WishlistMemberBase): ...


class WishlistMemberUpdateDB(BaseModel):
    wishlist_id: PositiveInt | None = None
    user_id: PositiveInt | None = None


class WishlistMemberRead(Id, WishlistMemberBase):
    model_config = ConfigDict(from_attributes=True)
