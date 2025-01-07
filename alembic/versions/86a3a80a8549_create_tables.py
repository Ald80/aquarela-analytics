"""create tables

Revision ID: 86a3a80a8549
Revises: 
Create Date: 2025-01-04 18:21:02.993351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '86a3a80a8549'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('cargo',
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('nome', sa.String(255), nullable=False),
                    sa.Column('cd_codigo', sa.String(50), nullable=False, unique=True),
                    sa.Column('salario', sa.Float, nullable=False))

    op.create_table('lider',
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('nome', sa.String(255), nullable=False),
                    sa.Column('matricula', sa.String(50), nullable=False, unique=True))

    op.create_table('status_colaborador',
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('nome', sa.String(255), nullable=False),
                    sa.Column('cd_status', sa.String(50), nullable=False, unique=True))

    op.create_table(
        'colaborador', sa.Column('id', sa.Integer, primary_key=True,
                                 autoincrement=True),
        sa.Column('nome', sa.String(255), nullable=False),
        sa.Column('sobrenome', sa.String(255), nullable=False),
        sa.Column('matricula', sa.String(50), nullable=False, unique=True),
        sa.Column('senha', sa.String(255), nullable=False),
        sa.Column('id_cargo', sa.Integer, sa.ForeignKey('cargo.id'), nullable=False),
        sa.Column('id_status',
                  sa.Integer,
                  sa.ForeignKey('status_colaborador.id'),
                  nullable=False),
        sa.Column('id_lider', sa.Integer, sa.ForeignKey('lider.id'), nullable=False))


def downgrade() -> None:
    op.execute('DROP TABLE colaborador CASCADE;')
    op.execute('DROP TABLE status_colaborador CASCADE;')
    op.execute('DROP TABLE lider CASCADE;')
    op.execute('DROP TABLE cargo CASCADE;')
