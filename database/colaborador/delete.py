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
from .read import fetch_colaborador_by_matricula
from enum import Enum
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def exclude_colaborador(matricula_colaborador: str, db: Session):
    try:
        colaborador = fetch_colaborador_by_matricula(matricula_colaborador, db)
        if not colaborador:
            # raise Exception("Colaborador não encontrado.")
            raise NotFoundError("Colaborador não encontrado.")
        db.delete(colaborador)
        db.commit()
    except NotFoundError as e:
        raise e
    except Exception as e:
        # print(e)
        raise ServerError(f"{e}")
    