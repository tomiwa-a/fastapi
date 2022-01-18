"""create votes table

Revision ID: b23ffb34a975
Revises: 39521cc137e4
Create Date: 2022-01-18 10:10:43.205105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b23ffb34a975'
down_revision = '39521cc137e4'
branch_labels = None
depends_on = None


def upgrade():
    votes = op.create_table("votes", 
    sa.Column("user_id",  sa.Integer(), nullable=False, primary_key=True),
    sa.Column("post_id", sa.Integer(), nullable=False, primary_key=True)
    )

    op.create_foreign_key("votes_users_fk", "votes", "users", ['user_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key("votes_post_fk", "votes", "posts", ['post_id'], ['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("votes_users_fk", table_name="votes")
    op.drop_constraint("votes_post_fk", table_name="votes")
    op.drop_table("votes")
