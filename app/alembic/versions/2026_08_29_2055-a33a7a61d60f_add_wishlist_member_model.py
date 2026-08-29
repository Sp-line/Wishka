"""add wishlist member model

Revision ID: a33a7a61d60f
Revises: cd7165dae2ac
Create Date: 2026-08-29 20:55:56.160669

"""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "a33a7a61d60f"
down_revision: str | Sequence[str] | None = "cd7165dae2ac"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("wishlist_members",
                    sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("wishlist_id", sa.Integer(), nullable=False),
    sa.Column("user_id", sa.Integer(), nullable=False),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_wishlist_members_user_id_users"), ondelete="CASCADE"),
    sa.ForeignKeyConstraint(["wishlist_id"], ["wishlists.id"], name=op.f("fk_wishlist_members_wishlist_id_wishlists"), ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id", name=op.f("pk_wishlist_members")),
    sa.UniqueConstraint("wishlist_id", "user_id", name="uq_wishlist_members_wishlist_id_user_id"),
    )
    op.create_index(op.f("ix_wishlist_members_user_id"), "wishlist_members", ["user_id"], unique=False)
    op.create_index(op.f("ix_wishlist_members_wishlist_id"), "wishlist_members", ["wishlist_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_wishlist_members_wishlist_id"), table_name="wishlist_members")
    op.drop_index(op.f("ix_wishlist_members_user_id"), table_name="wishlist_members")
    op.drop_table("wishlist_members")
