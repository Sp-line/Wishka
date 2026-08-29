from app.constants.db import PostgresErrorCode
from app.exceptions.db import RelatedObjectNotFoundError
from app.exceptions.db import UniqueError
from app.exceptions.db import UniqueFieldError
from app.repositories.handlers.base import TableErrorHandler
from app.schemas.db import ConstraintRule

pk_wishlist_members = ConstraintRule(
    name="pk_wishlist_members",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueFieldError(field_name="id", table_name="wishlist_members"),
)

uq_wishlist_members_wishlist_id_user_id = ConstraintRule(
    name="uq_wishlist_members_wishlist_id_user_id",
    error_code=PostgresErrorCode.UNIQUE_VIOLATION,
    exception=UniqueError("wishlist_members", "wishlist_id", "user_id"),
)

fk_wishlist_members_wishlist_id_wishlists = ConstraintRule(
    name="fk_wishlist_members_wishlist_id_wishlists",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(
        field_name="wishlist_id",
        table_name="wishlist_members",
    ),
)

fk_wishlist_members_user_id_users = ConstraintRule(
    name="fk_wishlist_members_user_id_users",
    error_code=PostgresErrorCode.FOREIGN_KEY_VIOLATION,
    exception=RelatedObjectNotFoundError(
        field_name="user_id",
        table_name="wishlist_members",
    ),
)

wishlist_member_error_handler = TableErrorHandler(
    pk_wishlist_members,
    uq_wishlist_members_wishlist_id_user_id,
    fk_wishlist_members_wishlist_id_wishlists,
    fk_wishlist_members_user_id_users,
)
