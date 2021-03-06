"""empty message

Revision ID: 86c9c2547c2a
Revises: a04b6a31831a
Create Date: 2019-12-22 18:15:21.382593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c9c2547c2a'
down_revision = 'a04b6a31831a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logging',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('request', sa.String(length=200), nullable=False),
    sa.Column('null_api', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logging')
    # ### end Alembic commands ###
