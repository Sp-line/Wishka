"""add username for user

Revision ID: 9514c57feec7
Revises: 157b177971bb
Create Date: 2026-08-29 23:14:32.404387

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "9514c57feec7"
down_revision: str | Sequence[str] | None = "157b177971bb"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("users", sa.Column("username", sa.String(length=20), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "username")
