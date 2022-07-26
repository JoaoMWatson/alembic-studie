"""alteracao pessoa email 50 char

Revision ID: a52a33be842d
Revises: d2c11800d3c5
Create Date: 2022-07-20 10:50:58.318736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a52a33be842d'
down_revision = 'd2c11800d3c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.alter_column('email',
                existing_type=sa.VARCHAR(length=100),
                type_=sa.String(length=50),
                existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.alter_column('email',
                existing_type=sa.VARCHAR(length=50),
                type_=sa.String(length=100),
                existing_nullable=False)
    # ### end Alembic commands ###
