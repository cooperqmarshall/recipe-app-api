"""empty message

Revision ID: 4464561a3584
Revises: 03b6c46d6f45
Create Date: 2022-03-27 20:43:06.444532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4464561a3584'
down_revision = '03b6c46d6f45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('instructions', sa.Text(), nullable=True))
    op.add_column('Recipe', sa.Column('ingredients', sa.Text(), nullable=True))
    op.add_column('Recipe', sa.Column('image_urls', sa.Text(), nullable=True))
    op.drop_column('Recipe', 'data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('data', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('Recipe', 'image_urls')
    op.drop_column('Recipe', 'ingredients')
    op.drop_column('Recipe', 'instructions')
    # ### end Alembic commands ###
