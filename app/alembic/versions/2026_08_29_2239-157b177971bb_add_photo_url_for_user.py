"""add photo url for user

Revision ID: 157b177971bb
Revises: 4e573b810bed
Create Date: 2026-08-29 22:39:03.221092

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "157b177971bb"
down_revision: str | Sequence[str] | None = "4e573b810bed"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("users", sa.Column("photo_url", sa.String(length=2048), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "photo_url")
