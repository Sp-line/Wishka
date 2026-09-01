from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002

from app.core.models.wishlist_member import WishlistMember
from app.repositories.base import RepositoryBase
from app.repositories.handlers.reservation import reservation_error_handler
from app.schemas.wishlist_member import WishlistMemberCreateDB
from app.schemas.wishlist_member import WishlistMemberUpdateDB


class WishlistMemberRepository(
    RepositoryBase[
        WishlistMember,
        WishlistMemberCreateDB,
        WishlistMemberUpdateDB,
    ],
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            model=WishlistMember,
            session=session,
            table_error_handler=reservation_error_handler,
        )

    async def get_by_user_and_wishlist(
        self,
        user_id: int,
        wishlist_id: int,
    ) -> WishlistMember | None:
        stmt = select(WishlistMember).where(
            WishlistMember.user_id == user_id,
            WishlistMember.wishlist_id == wishlist_id,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()
