"""empty message

Revision ID: 7e8d7e7addd4
Revises: 
Create Date: 2018-01-26 03:10:24.209914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e8d7e7addd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('available_products',
    sa.Column('product_id', sa.String(length=20), nullable=False),
    sa.Column('consumer_id', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('product_id', 'consumer_id')
    )
    op.create_table('issued_tokens',
    sa.Column('product_id', sa.String(length=20), nullable=False),
    sa.Column('consumer_id', sa.String(length=20), nullable=False),
    sa.Column('valid_from', sa.DateTime(), nullable=False),
    sa.Column('valid_to', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('product_id', 'consumer_id', 'valid_from', 'valid_to')
    )
    op.create_table('used_products',
    sa.Column('product_id', sa.String(length=20), nullable=False),
    sa.Column('comsumer_id', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('product_id', 'comsumer_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('used_products')
    op.drop_table('issued_tokens')
    op.drop_table('available_products')
    # ### end Alembic commands ###
