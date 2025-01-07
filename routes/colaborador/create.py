from fastapi import Depends, APIRouter
from models.colaborador import Colaborador
from schemas.colaborador import ColaboradorResponse, ColaboradorCreate
from database.session_db import SessionLocal, get_db
from database.colaborador.create import insert_colaborador

router = APIRouter(prefix="/colaborador", tags=["colaborador"])


@router.post("/", response_model=ColaboradorResponse)
def create_colaborador(colaborador_create: ColaboradorCreate,
                       db: SessionLocal = Depends(get_db)):
    colaborador: Colaborador = insert_colaborador(colaborador_create, db)
    return colaborador
