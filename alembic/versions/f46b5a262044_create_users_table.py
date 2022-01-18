"""create users table

Revision ID: f46b5a262044
Revises: 1d129f84cb16
Create Date: 2022-01-18 09:55:10.599596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f46b5a262044'
down_revision = '1d129f84cb16'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", 
    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("email", sa.String(), nullable=False),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
    sa.UniqueConstraint("email")
    )


def downgrade():
    op.drop_table("users")
