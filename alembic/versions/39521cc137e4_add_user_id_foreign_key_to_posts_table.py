"""add user_id foreign key to posts table

Revision ID: 39521cc137e4
Revises: f46b5a262044
Create Date: 2022-01-18 10:01:18.409092

"""
from unicodedata import name
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39521cc137e4'
down_revision = 'f46b5a262044'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table= "posts", referent_table="users", local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE' )


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "user_id")
