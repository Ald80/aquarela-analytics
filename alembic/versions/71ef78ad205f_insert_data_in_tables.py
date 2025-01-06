"""insert data in tables

Revision ID: 71ef78ad205f
Revises: 86a3a80a8549
Create Date: 2025-01-04 18:59:12.108625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from passlib.context import CryptContext

# revision identifiers, used by Alembic.
revision: str = '71ef78ad205f'
down_revision: Union[str, None] = '86a3a80a8549'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def insert_data():
    cargo_table = table('cargo', 
        column('id', sa.Integer),
        column('nome', sa.String),
        column('cd_codigo', sa.String),
        column('salario', sa.Float)
    )

    lider_table = table('lider',
        column('id', sa.Integer),
        column('nome', sa.String),
        column('matricula', sa.String)
    )

    status_colaborador_table = table('status_colaborador',
        column('id', sa.Integer),
        column('nome', sa.String),
        column('cd_status', sa.String)
    )

    colaborador_table = table('colaborador',
        column('id', sa.Integer),
        column('nome', sa.String),
        column('sobrenome', sa.String),
        column('matricula', sa.String),
        column('senha', sa.String),
        column('id_cargo', sa.Integer),
        column('id_status', sa.Integer),
        column('id_lider', sa.Integer)
    )
    pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

    op.bulk_insert(cargo_table, [
        {'id': 1, 'nome': 'Gerente', 'cd_codigo': 'C001', 'salario': 8000.0},
        {'id': 2, 'nome': 'Analista', 'cd_codigo': 'C002', 'salario': 5000.0},
        {'id': 3, 'nome': 'Assistente', 'cd_codigo': 'C003', 'salario': 3000.0}
    ])

    op.bulk_insert(lider_table, [
        {'id': 1, 'nome': 'Carlos Silva', 'matricula': 'L001'},
        {'id': 2, 'nome': 'Ana Souza', 'matricula': 'L002'}
    ])

    op.bulk_insert(status_colaborador_table, [
        {'id': 1, 'nome': 'Ativo', 'cd_status': 'S001'},
        {'id': 2, 'nome': 'Demitido', 'cd_status': 'S002'},
        {'id': 3, 'nome': 'Afastado', 'cd_status': 'S003'}
    ])

    op.bulk_insert(colaborador_table, [
        {'id': 1, 'nome': 'João', 'sobrenome': 'Pereira', 'matricula': 'C001', 'senha': pwd_context.hash('123456'), 'id_cargo': 1, 'id_status': 1, 'id_lider': 1},
        {'id': 2, 'nome': 'Maria', 'sobrenome': 'Oliveira', 'matricula': 'C002', 'senha': pwd_context.hash('654321'), 'id_cargo': 2, 'id_status': 1, 'id_lider': 2},
        {'id': 3, 'nome': 'José', 'sobrenome': 'Silva', 'matricula': 'C003', 'senha': pwd_context.hash('abcdef'), 'id_cargo': 3, 'id_status': 2, 'id_lider': 1}
    ])

def upgrade() -> None:
    insert_data()


def downgrade() -> None:
    op.execute('DELETE from colaborador CASCADE;')
    op.execute('DELETE from cargo CASCADE;')
    op.execute('DELETE from lider CASCADE;')
    op.execute('DELETE from status_colaborador CASCADE;')
