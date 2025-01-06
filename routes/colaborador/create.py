from fastapi import FastAPI, Depends, APIRouter, HTTPException, Response
from schemas.colaborador import ColaboradorResponse, ColaboradorUpdate, ColaboradorCreate, ColaboradorAlterPassword, ColaboradorPromotion
from database.session_db import SessionLocal, get_db
from database.colaborador.create import insert_colaborador

from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from exceptions.customized_exceptions import ServerError, NotFoundError, ConflictError

router = APIRouter(prefix="/colaborador", tags=["colaborador"])

@router.post("/", response_model=ColaboradorResponse)
def create_colaborador(colaborador_create: ColaboradorCreate, db: SessionLocal = Depends(get_db)):
    try:
        colaborador = insert_colaborador(colaborador_create, db)
    except IntegrityError:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Erro de integridade: dado já existe no banco de dados.")
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=f"Erro interno no servidor. {e}")
    return colaborador
