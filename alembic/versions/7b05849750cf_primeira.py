"""primeira

Revision ID: 7b05849750cf
Revises: 
Create Date: 2022-07-20 09:53:18.355276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b05849750cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('pessoa')
