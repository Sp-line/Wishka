"""add wishlist owner fk index

Revision ID: 17796191380a
Revises: 98118708d1b6
Create Date: 2026-08-29 19:45:49.992774

"""
from collections.abc import Sequence

from alembic import op

revision: str = "17796191380a"
down_revision: str | Sequence[str] | None = "98118708d1b6"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_index(op.f("ix_wishlists_owner_id"), "wishlists", ["owner_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_wishlists_owner_id"), table_name="wishlists")
