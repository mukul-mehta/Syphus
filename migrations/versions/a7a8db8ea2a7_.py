"""empty message

Revision ID: a7a8db8ea2a7
Revises: 48cfa793003b
Create Date: 2019-12-13 02:35:06.445420

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a7a8db8ea2a7'
down_revision = '48cfa793003b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('newsletter',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('publish_date', sa.String(length=255), nullable=True),
        sa.Column('newsletter_content', sa.Text(), nullable=True),
        sa.Column('upload_time', sa.DateTime(), nullable=True),
        sa.Column('cover_image_url', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('newsletter')
    # ### end Alembic commands ###
