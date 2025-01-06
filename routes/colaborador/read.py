from fastapi import FastAPI, Depends, APIRouter, HTTPException, Response
from schemas.colaborador import ColaboradorResponse, ColaboradorUpdate, ColaboradorCreate, ColaboradorAlterPassword, ColaboradorPromotion
from database.session_db import SessionLocal, get_db
from database.colaborador.read import fetch_all_colaboradores, fetch_colaborador_by_matricula
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from exceptions.customized_exceptions import ServerError, NotFoundError, ConflictError

router = APIRouter(prefix="/colaborador", tags=["colaborador"])

@router.get("/buscar-todos", response_model=list[ColaboradorResponse])
def get_colaboradores(db: SessionLocal = Depends(get_db)):
    colaboradores = fetch_all_colaboradores(db)
    return colaboradores
    
@router.get("/matricula/{matricula_colaborador}", response_model=ColaboradorResponse)
def get_by_matricula(matricula_colaborador: str, db: SessionLocal = Depends(get_db)):
    colaborador = fetch_colaborador_by_matricula(matricula_colaborador, db)
    if not colaborador:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Colaborador não encontrado.")
    print("colaborador")
    for key, value in vars(colaborador).items():
        print(f"{key}: {value}")
    print(colaborador)
    return colaborador
