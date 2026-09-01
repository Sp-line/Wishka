"""add role for wishlist member

Revision ID: a7adc96ff516
Revises: 9514c57feec7
Create Date: 2026-09-01 23:22:51.637819

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "a7adc96ff516"
down_revision: str | Sequence[str] | None = "9514c57feec7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("wishlist_members",
                  sa.Column("role", sa.Enum("OWNER", "PARTICIPANT", name="role", native_enum=False, length=32),
                            nullable=False))
    op.create_index("ix_one_owner_per_wishlist", "wishlist_members", ["wishlist_id"], unique=True,
                    postgresql_where=sa.text("role = 'OWNER'"))


def downgrade() -> None:
    op.drop_index("ix_one_owner_per_wishlist", table_name="wishlist_members",
                  postgresql_where=sa.text("role = 'OWNER'"))
    op.drop_column("wishlist_members", "role")
