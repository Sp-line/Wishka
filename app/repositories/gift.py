from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002

from app.core.models.gift import Gift
from app.repositories.base import RepositoryBase
from app.repositories.handlers.gift import gift_error_handler
from app.schemas.gift import GiftCreateDB
from app.schemas.gift import GiftUpdateDB


class GiftRepository(
    RepositoryBase[
        Gift,
        GiftCreateDB,
        GiftUpdateDB,
    ],
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            model=Gift,
            session=session,
            table_error_handler=gift_error_handler,
        )
