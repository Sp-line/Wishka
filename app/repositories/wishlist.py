from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002

from app.core.models.wishlist import Wishlist
from app.repositories.base import RepositoryBase
from app.repositories.handlers.reservation import reservation_error_handler
from app.schemas.wishlist import WishlistCreateDB
from app.schemas.wishlist import WishlistUpdateDB


class WishlistRepository(
    RepositoryBase[
        Wishlist,
        WishlistCreateDB,
        WishlistUpdateDB,
    ],
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            model=Wishlist,
            session=session,
            table_error_handler=reservation_error_handler,
        )
