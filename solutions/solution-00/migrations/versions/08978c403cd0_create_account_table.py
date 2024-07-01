"""create account table

Revision ID: 08978c403cd0
Revises: 78747e794fea
Create Date: 2024-07-01 14:06:09.566701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08978c403cd0'
down_revision: Union[str, None] = '78747e794fea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
