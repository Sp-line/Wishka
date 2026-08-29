"""add reservation model

Revision ID: cd7165dae2ac
Revises: 0deb1a9f5c72
Create Date: 2026-08-29 20:36:59.053019

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "cd7165dae2ac"
down_revision: str | Sequence[str] | None = "0deb1a9f5c72"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("reservations",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("quantity", sa.Integer(), server_default="1", nullable=False),
                    sa.Column("gift_id", sa.Integer(), nullable=False),
                    sa.Column("reserver_id", sa.Integer(), nullable=False),
                    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
                    sa.ForeignKeyConstraint(["gift_id"], ["gifts.id"], name=op.f("fk_reservations_gift_id_gifts"),
                                            ondelete="CASCADE"),
                    sa.ForeignKeyConstraint(["reserver_id"], ["users.id"],
                                            name=op.f("fk_reservations_reserver_id_users"), ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint("id", name=op.f("pk_reservations")),
                    sa.UniqueConstraint("gift_id", "reserver_id", name="uq_reservations_gift_id_reserver_id"),
                    )
    op.create_index(op.f("ix_reservations_gift_id"), "reservations", ["gift_id"], unique=False)
    op.create_index(op.f("ix_reservations_reserver_id"), "reservations", ["reserver_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_reservations_reserver_id"), table_name="reservations")
    op.drop_index(op.f("ix_reservations_gift_id"), table_name="reservations")
    op.drop_table("reservations")
