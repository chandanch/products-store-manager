"""product_image_table

Revision ID: faa55e3fff02
Revises: a6c7e7645754
Create Date: 2024-08-31 19:02:48.139180

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "faa55e3fff02"
down_revision: Union[str, None] = "a6c7e7645754"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "product_image",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("alternative_text", sa.String(length=100), nullable=False),
        sa.Column("url", sa.String(length=200), nullable=False),
        sa.Column("order", sa.Integer(), nullable=False),
        sa.Column("product_line_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_line_id"],
            ["product_line.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_unique_constraint(
        "unq_product_image_order_product_line_id_constraint",
        "product_image",
        ["order", "product_line_id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        "unq_product_line_sku_constraint", "product_line", ["sku"]
    )
    op.create_unique_constraint(
        "unq_product_line_order_product_id_constraint",
        "product_line",
        ["order", "product_id"],
    )
    op.create_unique_constraint("unq_product_slug_constraint", "product", ["slug"])
    op.create_unique_constraint("unq_product_name_constraint", "product", ["name"])
    op.create_unique_constraint("unq_category_slug_constraint", "category", ["slug"])
    op.create_unique_constraint(
        "unq_category_name_level_constraint", "category", ["name", "level"]
    )
    op.drop_table("product_image")
    # ### end Alembic commands ###
