"""add recommendation query index

Revision ID: 220db7417f66
Revises: ff016e3bba01
Create Date: 2026-08-12
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "220db7417f66"
down_revision: Union[str, Sequence[str], None] = "ff016e3bba01"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "ix_recommendations_student_subject_topic",
        "recommendations",
        [
            "student_id",
            "subject_id",
            "topic_id"
        ],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(
        "ix_recommendations_student_subject_topic",
        table_name="recommendations"
    )