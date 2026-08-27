"""add oauth account model

Revision ID: b1903b069cb2
Revises: 26fcfdb3db11
Create Date: 2026-08-27 18:04:04.146036

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "b1903b069cb2"
down_revision: str | Sequence[str] | None = "26fcfdb3db11"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("o_auth_accounts",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("user_id", sa.Integer(), nullable=False),
                    sa.Column("oauth_name", sa.String(length=100), nullable=False),
                    sa.Column("access_token", sa.String(length=1024), nullable=False),
                    sa.Column("expires_at", sa.Integer(), nullable=True),
                    sa.Column("refresh_token", sa.String(length=1024), nullable=True),
                    sa.Column("account_id", sa.String(length=320), nullable=False),
                    sa.Column("account_email", sa.String(length=320), nullable=False),
                    sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("fk_o_auth_accounts_user_id_users"),
                                            ondelete="cascade"),
                    sa.PrimaryKeyConstraint("id", name=op.f("pk_o_auth_accounts")),
                    )
    op.create_index(op.f("ix_o_auth_accounts_account_id"), "o_auth_accounts", ["account_id"], unique=False)
    op.create_index(op.f("ix_o_auth_accounts_oauth_name"), "o_auth_accounts", ["oauth_name"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_o_auth_accounts_oauth_name"), table_name="o_auth_accounts")
    op.drop_index(op.f("ix_o_auth_accounts_account_id"), table_name="o_auth_accounts")
    op.drop_table("o_auth_accounts")
