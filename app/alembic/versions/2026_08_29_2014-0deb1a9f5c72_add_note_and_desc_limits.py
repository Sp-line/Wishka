"""add note and desc limits

Revision ID: 0deb1a9f5c72
Revises: 17796191380a
Create Date: 2026-08-29 20:14:00.861415

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0deb1a9f5c72"
down_revision: str | Sequence[str] | None = "17796191380a"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.alter_column("gifts", "note",
               existing_type=sa.TEXT(),
               type_=sa.String(length=300),
               existing_nullable=True)
    op.alter_column("wishlists", "description",
               existing_type=sa.TEXT(),
               type_=sa.String(length=500),
               existing_nullable=True)


def downgrade() -> None:
    op.alter_column("wishlists", "description",
               existing_type=sa.String(length=500),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column("gifts", "note",
               existing_type=sa.String(length=300),
               type_=sa.TEXT(),
               existing_nullable=True)
