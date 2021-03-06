"""empty message

Revision ID: 27cd11cac662
Revises: d4a5e489f3f9
Create Date: 2017-02-22 16:29:28.539744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27cd11cac662'
down_revision = 'd4a5e489f3f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user_profile', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
