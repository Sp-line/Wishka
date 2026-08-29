from app.constants.db import PostgresErrorCode
from app.exceptions.db import RelatedObjectNotFoundError
from app.exceptions.db import UniqueFieldError
from app.repositories.handlers.base import TableErrorHandler
from app.schemas.db import ConstraintRule

pk_o_auth_accounts = ConstraintRule(
    name="pk_o_auth_accounts",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="id", table_name="o_auth_accounts"),
)

fk_o_auth_accounts_user_id_users = ConstraintRule(
    name="fk_o_auth_accounts_user_id_users",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(
        field_name="user_id",
        table_name="o_auth_accounts",
    ),
)

oauth_account_error_handler = TableErrorHandler(
    pk_o_auth_accounts,
    fk_o_auth_accounts_user_id_users,
)
