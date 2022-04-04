"""empty message

Revision ID: 93f63292c6ec
Revises: 
Create Date: 2022-03-29 19:28:14.780085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93f63292c6ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.Date(), nullable=True),
    sa.Column('assignation_date', sa.Date(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('private', sa.Boolean(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_recipe', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_recipe'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('my_recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_recipe', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_recipe'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_ingredient', sa.Integer(), nullable=True),
    sa.Column('id_recipe', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_ingredient'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['id_recipe'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_menu', sa.Integer(), nullable=True),
    sa.Column('id_recipe', sa.Integer(), nullable=True),
    sa.Column('selected_tag', sa.Integer(), nullable=False),
    sa.Column('selected_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_menu'], ['menu.id'], ),
    sa.ForeignKeyConstraint(['id_recipe'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_menu')
    op.drop_table('recipe_ingredient')
    op.drop_table('my_recipe')
    op.drop_table('comment')
    op.drop_table('recipe')
    op.drop_table('menu')
    op.drop_table('user')
    op.drop_table('ingredient')
    # ### end Alembic commands ###
