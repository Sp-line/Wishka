"""add wishlist model

Revision ID: f080d8c3edac
Revises: b1903b069cb2
Create Date: 2026-08-29 16:35:09.160321

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "f080d8c3edac"
down_revision: str | Sequence[str] | None = "b1903b069cb2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("wishlists",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("title", sa.String(length=20), nullable=False),
                    sa.Column("description", sa.Text(), nullable=True),
                    sa.Column("invite_token", sa.String(length=64), nullable=False),
                    sa.Column("owner_id", sa.Integer(), nullable=False),
                    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.ForeignKeyConstraint(["owner_id"], ["users.id"], name=op.f("fk_wishlists_owner_id_users"),
                                            ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint("id", name=op.f("pk_wishlists")),
                    sa.UniqueConstraint("invite_token", name=op.f("uq_wishlists_invite_token")),
                    )


def downgrade() -> None:
    op.drop_table("wishlists")
