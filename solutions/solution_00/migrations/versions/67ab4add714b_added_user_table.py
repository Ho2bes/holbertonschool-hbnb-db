"""Added user table

Revision ID: 67ab4add714b
Revises: e11ef3e3e6fc
Create Date: 2024-07-02 10:48:56.208823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67ab4add714b'
down_revision: Union[str, None] = 'e11ef3e3e6fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
