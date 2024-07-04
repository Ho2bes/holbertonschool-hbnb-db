"""Added user table

Revision ID: e11ef3e3e6fc
Revises: a8ada8744aad
Create Date: 2024-07-01 15:41:03.890134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e11ef3e3e6fc'
down_revision: Union[str, None] = 'a8ada8744aad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
