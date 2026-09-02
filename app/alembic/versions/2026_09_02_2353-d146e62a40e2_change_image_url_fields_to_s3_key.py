"""change image url fields to s3 key

Revision ID: d146e62a40e2
Revises: a7adc96ff516
Create Date: 2026-09-02 23:53:03.189008

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "d146e62a40e2"
down_revision: str | Sequence[str] | None = "a7adc96ff516"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("gifts", sa.Column("image_s3_key", sa.String(length=255), nullable=True))
    op.drop_column("gifts", "image_url")
    op.add_column("users", sa.Column("avatar_s3_key", sa.String(length=255), nullable=True))
    op.drop_column("users", "photo_url")


def downgrade() -> None:
    op.add_column("users", sa.Column("photo_url", sa.VARCHAR(length=2048), autoincrement=False, nullable=True))
    op.drop_column("users", "avatar_s3_key")
    op.add_column("gifts", sa.Column("image_url", sa.VARCHAR(length=2048), autoincrement=False, nullable=True))
    op.drop_column("gifts", "image_s3_key")
