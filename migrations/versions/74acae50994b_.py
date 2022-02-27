"""empty message

Revision ID: 74acae50994b
Revises: c134e4a7444b
Create Date: 2022-02-23 18:46:58.097668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74acae50994b'
down_revision = 'c134e4a7444b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_name', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    # ### end Alembic commands ###