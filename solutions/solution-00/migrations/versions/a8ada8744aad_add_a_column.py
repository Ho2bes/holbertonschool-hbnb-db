"""Add a column

Revision ID: a8ada8744aad
Revises: 4fa0ea0fc3b5
Create Date: 2024-07-01 15:15:19.010911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8ada8744aad'
down_revision: Union[str, None] = '4fa0ea0fc3b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
