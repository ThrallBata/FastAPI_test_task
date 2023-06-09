"""rename id

Revision ID: 5edf5d3d897b
Revises: 
Create Date: 2023-06-06 16:53:47.721442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5edf5d3d897b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workers',
    sa.Column('worker_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('salary', sa.Float(), nullable=False),
    sa.Column('promotion_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('worker_id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workers')
    # ### end Alembic commands ###
