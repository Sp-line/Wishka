from sqlalchemy.ext.asyncio import AsyncSession  # noqa: TC002

from app.core.models.reservation import Reservation
from app.repositories.base import RepositoryBase
from app.repositories.handlers.reservation import reservation_error_handler
from app.schemas.reservation import ReservationCreateDB
from app.schemas.reservation import ReservationUpdateDB


class ReservationRepository(
    RepositoryBase[
        Reservation,
        ReservationCreateDB,
        ReservationUpdateDB,
    ],
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(
            model=Reservation,
            session=session,
            table_error_handler=reservation_error_handler,
        )
