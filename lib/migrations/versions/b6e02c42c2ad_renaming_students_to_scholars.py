"""Renaming students to scholars

Revision ID: b6e02c42c2ad
Revises: 791279dd0760
Create Date: 2023-12-07 22:54:52.131440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e02c42c2ad'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
