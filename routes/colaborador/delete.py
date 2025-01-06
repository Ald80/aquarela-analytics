from fastapi import FastAPI, Depends, APIRouter, HTTPException, Response
from schemas.colaborador import ColaboradorResponse, ColaboradorUpdate, ColaboradorCreate, ColaboradorAlterPassword, ColaboradorPromotion
from database.session_db import SessionLocal, get_db
from database.colaborador.delete import exclude_colaborador
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from exceptions.customized_exceptions import ServerError, NotFoundError, ConflictError

router = APIRouter(prefix="/colaborador", tags=["colaborador"])

@router.delete("/matricula/{matricula_colaborador}")
def delete_colaborador(matricula_colaborador: str, db: SessionLocal = Depends(get_db)):
    try:
        exclude_colaborador(matricula_colaborador, db)
        return {"message": "Colaborador excluido."}
    except NotFoundError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=e.message)
    except ServerError as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=e.message)
