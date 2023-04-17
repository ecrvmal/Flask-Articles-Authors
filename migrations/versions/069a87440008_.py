"""empty message

Revision ID: 069a87440008
Revises: 0b6890df11ce
Create Date: 2023-04-17 10:11:03.238537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '069a87440008'
down_revision = '0b6890df11ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_staff', sa.Boolean(), nullable=True))
        batch_op.drop_column('birth_year')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birth_year', sa.INTEGER(), nullable=True))
        batch_op.drop_column('is_staff')

    # ### end Alembic commands ###
