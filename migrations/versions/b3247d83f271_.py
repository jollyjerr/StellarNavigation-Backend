"""empty message

Revision ID: b3247d83f271
Revises: d89027cd58e6
Create Date: 2019-09-30 19:52:12.336163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3247d83f271'
down_revision = 'd89027cd58e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('large_celestial', sa.Column('color', sa.String(length=30), nullable=True))
    op.add_column('small_celestial', sa.Column('color', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('small_celestial', 'color')
    op.drop_column('large_celestial', 'color')
    # ### end Alembic commands ###