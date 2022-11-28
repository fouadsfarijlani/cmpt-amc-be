"""added relationship vacancy desciption and descriptio tags

Revision ID: 5a87e6107e56
Revises: 0cd045d2fe49
Create Date: 2022-11-28 21:23:11.695058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a87e6107e56'
down_revision = '0cd045d2fe49'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacancy_description', sa.Column('vacancy_description_tag_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'vacancy_description', 'vacancy_description_tag', ['vacancy_description_tag_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vacancy_description', type_='foreignkey')
    op.drop_column('vacancy_description', 'vacancy_description_tag_id')
    # ### end Alembic commands ###
