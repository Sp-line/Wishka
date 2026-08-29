from app.constants.db import PostgresErrorCode
from app.exceptions.db import RelatedObjectNotFoundError
from app.exceptions.db import UniqueFieldError
from app.repositories.handlers.base import TableErrorHandler
from app.schemas.db import ConstraintRule

pk_gifts = ConstraintRule(
    name="pk_gifts",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="id", table_name="gifts"),
)

fk_gifts_wishlist_id_wishlists = ConstraintRule(
    name="fk_gifts_wishlist_id_wishlists",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(field_name="wishlist_id", table_name="gifts"),
)

gift_error_handler = TableErrorHandler(
    pk_gifts,
    fk_gifts_wishlist_id_wishlists,
)
