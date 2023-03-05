"""empty message

Revision ID: 1b4a8f295d5e
Revises: 4f5ff7d08b53
Create Date: 2023-03-05 16:27:50.170740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b4a8f295d5e'
down_revision = '4f5ff7d08b53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ass_post_category',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['post_category.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['user_posts.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ass_post_category')
    # ### end Alembic commands ###
