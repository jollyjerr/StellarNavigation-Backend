"""empty message

Revision ID: 689136ffd698
Revises: b3247d83f271
Create Date: 2019-10-01 11:07:45.195837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '689136ffd698'
down_revision = 'b3247d83f271'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stellar_system', sa.Column('stud', sa.String(length=128)))
    op.create_unique_constraint(None, 'stellar_system', ['stud'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stellar_system', type_='unique')
    op.drop_column('stellar_system', 'stud')
    # ### end Alembic commands ###