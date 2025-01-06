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
from .read import fetch_colaborador_by_matricula, fetch_status_colaborador_by_id

from enum import Enum
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

class StatusColaboradorEnum(Enum):
    Ativo = 1
    Demitido = 2
    Afastado = 3

def modify_colaborador(matricula_colaborador: str, colaborador_update: ColaboradorUpdate, db: Session):
    try:
        colaborador = fetch_colaborador_by_matricula(matricula_colaborador, db)
        if not colaborador:
            raise Exception("Colaborador não encontrado.")
        
        colaborador_data = colaborador_update.model_dump(exclude_unset=True)
        for key, value in colaborador_data.items():
            setattr(colaborador, key, value)

        db.commit()
        db.refresh(colaborador)
    except Exception as e:
        raise e
    
    return colaborador

def alter_senha(colaborador_alter_password: ColaboradorAlterPassword, db: Session):
    try:
        colaborador = fetch_colaborador_by_matricula(colaborador_alter_password.matricula, db)
        if not colaborador:
            raise NotFoundError("Colaborador não encontrado.")
        hashed_password = pwd_context.hash(colaborador_alter_password.senha)
        colaborador.senha = hashed_password
        db.commit()
        db.refresh(colaborador)
    except NotFoundError as e:
        raise e
    except Exception as e:
        raise ServerError(f"{e}")

def update_promotion(matricula_colaborador: str, colaborador_promotion: ColaboradorPromotion, db: Session):
    try:
        colaborador = fetch_colaborador_by_matricula(matricula_colaborador, db)
        if not colaborador:
            raise NotFoundError("Colaborador não encontrado.")
        if colaborador.id_status == StatusColaboradorEnum.Demitido.value:
            raise ConflictError("Colaborador demitido não pode ser promovido.")
        colaborador_data = colaborador_promotion.model_dump(exclude_unset=True)
        for key, value in colaborador_data.items():
            setattr(colaborador, key, value)
        db.commit()
        db.refresh(colaborador)
    except NotFoundError as e:
        raise e
    except ConflictError as e:
        raise e 
    except Exception as e:
        raise ServerError(f"{e}")
    
    return colaborador

def soft_delete_colaborador(matricula_colaborador: str, db: Session):
    try:
        colaborador = fetch_colaborador_by_matricula(matricula_colaborador, db)
        if not colaborador:
            raise NotFoundError("Colaborador não encontrado.")
        print("StatusColaboradorEnum.Demitido.value")
        print(StatusColaboradorEnum.Demitido.value)
        status_colaborador = fetch_status_colaborador_by_id(StatusColaboradorEnum.Demitido.value, db)
        for key, value in vars(status_colaborador).items():
            print(f"{key}: {value}")

        if colaborador.id_status == status_colaborador.id:
            raise ConflictError("Colaborador já está demitido.")
        colaborador.id_status = status_colaborador.id
        db.commit()
        db.refresh(colaborador)
    except NotFoundError as e:
        raise e
    except ConflictError as e:
        raise e 
    except Exception as e:
        raise ServerError(f"{e}")
    return colaborador
