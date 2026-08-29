from app.constants.db import PostgresErrorCode
from app.exceptions.db import RelatedObjectNotFoundError
from app.exceptions.db import UniqueError
from app.exceptions.db import UniqueFieldError
from app.repositories.handlers.base import TableErrorHandler
from app.schemas.db import ConstraintRule

pk_reservations = ConstraintRule(
    name="pk_reservations",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="id", table_name="reservations"),
)

uq_reservations_gift_id_reserver_id = ConstraintRule(
    name="uq_reservations_gift_id_reserver_id",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueError("reservations", "gift_id", "reserver_id"),
)

fk_reservations_gift_id_gifts = ConstraintRule(
    name="fk_reservations_gift_id_gifts",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(
        field_name="gift_id",
        table_name="reservations",
    ),
)

fk_reservations_reserver_id_users = ConstraintRule(
    name="fk_reservations_reserver_id_users",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(
        field_name="reserver_id",
        table_name="reservations",
    ),
)

reservation_error_handler = TableErrorHandler(
    pk_reservations,
    uq_reservations_gift_id_reserver_id,
    fk_reservations_gift_id_gifts,
    fk_reservations_reserver_id_users,
)
