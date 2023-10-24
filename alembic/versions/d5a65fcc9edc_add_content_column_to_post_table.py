"""add content column to post table

Revision ID: d5a65fcc9edc
Revises: e51ef0319c5d
Create Date: 2023-10-24 11:26:24.414944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5a65fcc9edc'
down_revision: Union[str, None] = 'e51ef0319c5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
