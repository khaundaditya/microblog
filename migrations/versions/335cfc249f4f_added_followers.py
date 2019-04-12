"""added followers

Revision ID: 335cfc249f4f
Revises: c8534331f7c6
Create Date: 2019-04-12 06:32:14.987449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335cfc249f4f'
down_revision = 'c8534331f7c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
