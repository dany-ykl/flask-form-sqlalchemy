"""empty message

Revision ID: 40f58b15ecd0
Revises: d164dcdd5e18
Create Date: 2022-02-08 12:56:38.763088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '40f58b15ecd0'
down_revision = 'd164dcdd5e18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datasources', sa.Column('description', sa.String(length=150), nullable=True))
    op.add_column('datasources', sa.Column('ref_auth_type', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'datasources', 'auth_type', ['ref_auth_type'], ['guid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'datasources', type_='foreignkey')
    op.drop_column('datasources', 'ref_auth_type')
    op.drop_column('datasources', 'description')
    # ### end Alembic commands ###
