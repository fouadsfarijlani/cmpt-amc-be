"""added date attribute to vacancy

Revision ID: 18ffaf8e3cb5
Revises: ae1ef034aafb
Create Date: 2022-11-28 22:03:37.999111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18ffaf8e3cb5'
down_revision = 'ae1ef034aafb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacancy', sa.Column('date_created', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vacancy', 'date_created')
    # ### end Alembic commands ###