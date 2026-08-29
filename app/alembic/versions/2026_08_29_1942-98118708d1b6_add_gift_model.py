"""add gift model

Revision ID: 98118708d1b6
Revises: f080d8c3edac
Create Date: 2026-08-29 19:42:28.445359

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "98118708d1b6"
down_revision: str | Sequence[str] | None = "f080d8c3edac"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("gifts",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("title", sa.String(length=30), nullable=False),
                    sa.Column("priority", sa.SmallInteger(), nullable=False),
                    sa.Column("quantity", sa.Integer(), server_default="1", nullable=False),
                    sa.Column("price", sa.Numeric(precision=10, scale=2), nullable=True),
                    sa.Column("url", sa.String(length=2048), nullable=True),
                    sa.Column("image_url", sa.String(length=2048), nullable=True),
                    sa.Column("note", sa.Text(), nullable=True),
                    sa.Column("wishlist_id", sa.Integer(), nullable=False),
                    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.ForeignKeyConstraint(["wishlist_id"], ["wishlists.id"],
                                            name=op.f("fk_gifts_wishlist_id_wishlists"), ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint("id", name=op.f("pk_gifts")),
                    )
    op.create_index(op.f("ix_gifts_wishlist_id"), "gifts", ["wishlist_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_gifts_wishlist_id"), table_name="gifts")
    op.drop_table("gifts")
