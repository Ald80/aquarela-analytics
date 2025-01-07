from sqlalchemy.orm import Session
from passlib.context import CryptContext
from exceptions.customized_exceptions import NotFoundError
from .colaborador.read import fetch_colaborador_by_matricula


def get_password_hashed(password: str):
    pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
    return pwd_context.hash(password)


def get_colaborador_by_matricula_or_404(matricula_colaborador: str, db: Session):
    colaborador = fetch_colaborador_by_matricula(matricula_colaborador, db)
    if not colaborador:
        raise NotFoundError("Colaborador não encontrado.")
    return colaborador


def update_instance(instance, data: dict):
    for key, value in data.items():
        setattr(instance, key, value)
