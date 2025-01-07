from fastapi import Depends, APIRouter
from schemas.colaborador import ColaboradorResponse
from database.session_db import SessionLocal, get_db
from database.colaborador.read import fetch_all_colaboradores
from database.utils import get_colaborador_by_matricula_or_404

router = APIRouter(prefix="/colaborador", tags=["colaborador"])


@router.get("/buscar-todos", response_model=list[ColaboradorResponse])
def get_colaboradores(db: SessionLocal = Depends(get_db)):
    colaboradores = fetch_all_colaboradores(db)
    return colaboradores


@router.get("/matricula/{matricula_colaborador}", response_model=ColaboradorResponse)
def get_by_matricula(matricula_colaborador: str, db: SessionLocal = Depends(get_db)):
    colaborador = get_colaborador_by_matricula_or_404(matricula_colaborador, db)
    return colaborador
