from __future__ import annotations

from typing import TYPE_CHECKING

from app.repositories.unit_of_work import UnitOfWork  # noqa: TC001
from app.repositories.wishlist import WishlistRepository  # noqa: TC001
from app.schemas.wishlist import WishlistCreateDB
from app.schemas.wishlist import WishlistCreateReq
from app.schemas.wishlist import WishlistRead

if TYPE_CHECKING:
    from pydantic import PositiveInt


class WishlistCreateUsage:
    def __init__(
        self,
        repository: WishlistRepository,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._repo = repository
        self._uow = unit_of_work

    async def __call__(
        self,
        data: WishlistCreateReq,
        owner_id: PositiveInt,
    ) -> WishlistRead:
        async with self._uow:
            wishlist_create_data = WishlistCreateDB(
                **data.model_dump(),
                owner_id=owner_id,
            )
            obj = await self._repo.create(wishlist_create_data)

            return WishlistRead.model_validate(obj)
