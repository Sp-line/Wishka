"""delete invite token form wishlist

Revision ID: dbd7a183aaca
Revises: 3f935c610e73
Create Date: 2026-09-03 01:25:20.350303

"""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "dbd7a183aaca"
down_revision: str | Sequence[str] | None = "3f935c610e73"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_constraint(op.f("uq_wishlists_invite_token"), "wishlists", type_="unique")
    op.drop_column("wishlists", "invite_token")


def downgrade() -> None:
    op.add_column("wishlists", sa.Column("invite_token", sa.VARCHAR(length=64), autoincrement=False, nullable=False))
    op.create_unique_constraint(op.f("uq_wishlists_invite_token"), "wishlists", ["invite_token"], postgresql_nulls_not_distinct=False)
