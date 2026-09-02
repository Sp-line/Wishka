"""add privacy and is reservable for wishlist

Revision ID: 3f935c610e73
Revises: d146e62a40e2
Create Date: 2026-09-03 00:27:58.067118

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "3f935c610e73"
down_revision: str | Sequence[str] | None = "d146e62a40e2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("wishlists", sa.Column("privacy",
                                         sa.Enum("PUBLIC", "PRIVATE", "WITH_LINK", "FRIENDS", name="wishlistprivacy",
                                                 native_enum=False, length=16), nullable=False))
    op.add_column("wishlists", sa.Column("is_reservable", sa.Boolean(), server_default="true", nullable=False))


def downgrade() -> None:
    op.drop_column("wishlists", "is_reservable")
    op.drop_column("wishlists", "privacy")
