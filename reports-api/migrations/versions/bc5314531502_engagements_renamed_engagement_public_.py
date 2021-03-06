"""engagements renamed engagement_public_link --> met_link

Revision ID: bc5314531502
Revises: c7fe197de4d4
Create Date: 2022-06-08 10:13:46.274185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc5314531502'
down_revision = 'c7fe197de4d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('engagements', sa.Column('met_link', sa.String(length=255), nullable=True))
    op.alter_column('engagements', 'staff_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('engagements', 'engagement_public_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('engagements', sa.Column('engagement_public_link', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.alter_column('engagements', 'staff_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('engagements', 'met_link')
    # ### end Alembic commands ###
