"""add currency for gift

Revision ID: 4e573b810bed
Revises: a33a7a61d60f
Create Date: 2026-08-29 21:14:40.237924

"""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "4e573b810bed"
down_revision: str | Sequence[str] | None = "a33a7a61d60f"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("gifts", sa.Column("currency", sa.Enum("UAH", "USD", "EUR", "PLN", "GBP", name="currency", native_enum=False), nullable=True))


def downgrade() -> None:
    op.drop_column("gifts", "currency")
