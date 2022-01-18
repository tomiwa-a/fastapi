"""create posts table

Revision ID: 1d129f84cb16
Revises: 
Create Date: 2022-01-17 16:41:54.947720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d129f84cb16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", 
    sa.Column("id", sa.Integer(), primary_key=True, nullable=False), 
    sa.Column("title", sa.String(), nullable=False), 
    sa.Column("content", sa.String(), nullable=False), 
    sa.Column("published", sa.Boolean(), nullable=False, default=False),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()'))
    )


def downgrade():
    op.drop_table("posts")
