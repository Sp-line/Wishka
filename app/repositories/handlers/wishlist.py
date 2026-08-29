from app.constants.db import PostgresErrorCode
from app.exceptions.db import RelatedObjectNotFoundError
from app.exceptions.db import UniqueFieldError
from app.repositories.handlers.base import TableErrorHandler
from app.schemas.db import ConstraintRule

pk_wishlists = ConstraintRule(
    name="pk_wishlists",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="id", table_name="wishlists"),
)

uq_wishlists_invite_token = ConstraintRule(
    name="uq_wishlists_invite_token",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="invite_token", table_name="wishlists"),
)

fk_wishlists_owner_id_users = ConstraintRule(
    name="fk_wishlists_owner_id_users",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(field_name="owner_id", table_name="wishlists"),
)

wishlist_error_handler = TableErrorHandler(
    pk_wishlists,
    uq_wishlists_invite_token,
    fk_wishlists_owner_id_users,
)
