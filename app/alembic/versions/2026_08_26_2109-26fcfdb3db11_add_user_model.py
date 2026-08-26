"""add user model

Revision ID: 26fcfdb3db11
Revises:
Create Date: 2026-08-26 21:09:13.258369

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "26fcfdb3db11"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.Column("email", sa.String(length=320), nullable=False),
                    sa.Column("hashed_password", sa.String(length=1024), nullable=False),
                    sa.Column("is_active", sa.Boolean(), nullable=False),
                    sa.Column("is_superuser", sa.Boolean(), nullable=False),
                    sa.Column("is_verified", sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
                    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
