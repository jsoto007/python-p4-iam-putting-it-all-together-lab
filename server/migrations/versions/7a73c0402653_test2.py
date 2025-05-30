"""test2

Revision ID: 7a73c0402653
Revises: 3678227ca81f
Create Date: 2025-05-05 21:12:29.171757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a73c0402653'
down_revision = '3678227ca81f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
