from app.constants.db import PostgresErrorCode
from app.exceptions.db import UniqueFieldError
from app.repositories.handlers.base import TableErrorHandler
from app.schemas.db import ConstraintRule

pk_users = ConstraintRule(
    name="pk_users",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="id", table_name="users"),
)

uq_users_email = ConstraintRule(
    name="uq_users_email",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="email", table_name="users"),
)

user_error_handler = TableErrorHandler(
    pk_users,
    uq_users_email,
)
