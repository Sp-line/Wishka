from __future__ import annotations

from typing import TYPE_CHECKING

from app.domain.wishlist import EnsureCanUpdateWishlist  # noqa: TC001
from app.exceptions.db import ObjectNotFoundError
from app.repositories.unit_of_work import UnitOfWork  # noqa: TC001
from app.repositories.wishlist import WishlistRepository  # noqa: TC001
from app.repositories.wishlist_member import WishlistMemberRepository  # noqa: TC001
from app.schemas.wishlist import WishlistRead
from app.schemas.wishlist import WishlistUpdateDB
from app.schemas.wishlist import WishlistUpdateReq

if TYPE_CHECKING:
    from pydantic import PositiveInt


class WishlistUpdateUsage:
    def __init__(
        self,
        repository: WishlistRepository,
        unit_of_work: UnitOfWork,
        wishlist_member_repository: WishlistMemberRepository,
        ensure_can_update_wishlist: EnsureCanUpdateWishlist,
    ) -> None:
        self._repo = repository
        self._uow = unit_of_work
        self._wishlist_member_repo = wishlist_member_repository
        self._ensure_can_update_wishlist = ensure_can_update_wishlist

    async def __call__(
        self,
        wishlist_id: PositiveInt,
        data: WishlistUpdateReq,
        current_user_id: PositiveInt,
    ) -> WishlistRead:
        async with self._uow:
            wishlist_member = await self._wishlist_member_repo.get_by_user_and_wishlist(
                user_id=current_user_id,
                wishlist_id=wishlist_id,
            )

            role = wishlist_member.role if wishlist_member is not None else None
            self._ensure_can_update_wishlist(role)

            update_data = WishlistUpdateDB(**data.model_dump())

            if not (
                updated_wishlist := await self._repo.update(wishlist_id, update_data)
            ):
                raise ObjectNotFoundError(table_name="wishlists", obj_id=wishlist_id)

            return WishlistRead.model_validate(updated_wishlist)
