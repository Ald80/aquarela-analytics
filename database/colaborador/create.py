from sqlalchemy.orm import Session
from models.colaborador import Colaborador as ColaboradorModel
from schemas.colaborador import ColaboradorCreate
from sqlalchemy.exc import IntegrityError
from database.utils import get_password_hashed


def insert_colaborador(colaborador_create: ColaboradorCreate, db: Session):
    colaborador_create.senha = get_password_hashed(colaborador_create.senha)
    new_colaborador = ColaboradorModel(**colaborador_create.model_dump())
    try:
        db.add(new_colaborador)
        db.commit()
        db.refresh(new_colaborador)
    except IntegrityError as e:
        db.rollback()
        raise e
    except Exception as e:
        raise e
    return new_colaborador
