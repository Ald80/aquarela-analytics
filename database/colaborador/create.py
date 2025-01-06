from sqlalchemy.orm import Session, joinedload
from models.colaborador import Colaborador as ColaboradorModel
from models.status_colaborador import StatusColaborador as StatusColaboradorModel
from models.cargo import Cargo as CargoModel
from models.status_colaborador import StatusColaborador as StatusColaboradorModel
from models.lider import Lider as LiderModel
from schemas.colaborador import ColaboradorCreate, ColaboradorUpdate, ColaboradorAlterPassword, ColaboradorPromotion
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from exceptions.customized_exceptions import ServerError, NotFoundError, ConflictError
from enum import Enum
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def insert_colaborador(colaborador_create: ColaboradorCreate, db: Session):
    hashed_password = pwd_context.hash(colaborador_create.senha)
    colaborador_create.senha = hashed_password
    print(colaborador_create.model_dump())
    new_colaborador = ColaboradorModel(**colaborador_create.model_dump())
    try:
        db.add(new_colaborador)
        db.commit()
        db.refresh(new_colaborador)
    except IntegrityError as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise e
    return new_colaborador

