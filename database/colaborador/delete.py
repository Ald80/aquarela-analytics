from sqlalchemy.orm import Session
from exceptions.customized_exceptions import ServerError, NotFoundError
from database.utils import get_colaborador_by_matricula_or_404


def exclude_colaborador(matricula_colaborador: str, db: Session):
    try:
        colaborador = get_colaborador_by_matricula_or_404(matricula_colaborador, db)
        db.delete(colaborador)
        db.commit()
    except NotFoundError as e:
        raise e
    except Exception as e:
        raise ServerError(f"{e}")
