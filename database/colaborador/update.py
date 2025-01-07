from sqlalchemy.orm import Session
from schemas.colaborador import ColaboradorUpdate, ColaboradorAlterPassword, ColaboradorPromotion

from exceptions.customized_exceptions import ServerError, NotFoundError, ConflictError
from .read import fetch_status_colaborador_by_id
from database.utils import get_colaborador_by_matricula_or_404, update_instance, get_password_hashed
from enum_types.colaborador_enum import StatusColaboradorEnum


def modify_colaborador(matricula_colaborador: str,
                       colaborador_update: ColaboradorUpdate, db: Session):
    try:
        colaborador = get_colaborador_by_matricula_or_404(matricula_colaborador, db)
        colaborador_data = colaborador_update.model_dump(exclude_unset=True)
        update_instance(colaborador, colaborador_data)
        db.commit()
        db.refresh(colaborador)
    except Exception as e:
        raise ServerError(f"{e}")

    return colaborador


def alter_senha(colaborador_alter_password: ColaboradorAlterPassword, db: Session):
    try:
        colaborador = get_colaborador_by_matricula_or_404(
            colaborador_alter_password.matricula, db)
        colaborador.senha = get_password_hashed(colaborador_alter_password.senha)
        db.commit()
        db.refresh(colaborador)
    except NotFoundError as e:
        raise e
    except Exception as e:
        raise ServerError(f"{e}")


def update_promotion(matricula_colaborador: str,
                     colaborador_promotion: ColaboradorPromotion, db: Session):
    try:
        colaborador = get_colaborador_by_matricula_or_404(matricula_colaborador, db)
        if StatusColaboradorEnum.is_demitido(colaborador.id_status):
            raise ConflictError("Colaborador demitido não pode ser promovido.")
        colaborador_data = colaborador_promotion.model_dump(exclude_unset=True)
        update_instance(colaborador, colaborador_data)
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
        colaborador = get_colaborador_by_matricula_or_404(matricula_colaborador, db)
        status_colaborador = fetch_status_colaborador_by_id(
            StatusColaboradorEnum.Demitido.value, db)
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
