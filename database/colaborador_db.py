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

class StatusColaboradorEnum(Enum):
    Ativo = 1
    Demitido = 2
    Afastado = 3

def fetch_all_colaboradores(db: Session):
    return db.query(ColaboradorModel).all()

def fetch_colaborador_by_matricula(matricula_colaborador: str, db: Session):
    return db.query(ColaboradorModel).filter(ColaboradorModel.matricula == matricula_colaborador).first()

def fetch_status_colaborador_by_id(id_status_colaborador: int, db: Session):
    return db.query(StatusColaboradorModel).filter(StatusColaboradorModel.id == id_status_colaborador).first()

# def fetch_colaborador_by_matricula_and_senha(matricula_colaborador: str, senha: str, db: Session):
# def fetch_colaborador_by_matricula_and_senha(matricula_colaborador: str, senha: str, db: Session):
#     return db.query(ColaboradorModel).filter(ColaboradorModel.matricula == matricula_colaborador, ColaboradorModel.senha == senha).first()

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
