"""Add a column

Revision ID: 4fa0ea0fc3b5
Revises: 08978c403cd0
Create Date: 2024-07-01 14:08:14.607674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fa0ea0fc3b5'
down_revision: Union[str, None] = '08978c403cd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
