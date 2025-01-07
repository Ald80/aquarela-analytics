from fastapi import Depends, APIRouter
from database.session_db import SessionLocal, get_db
from database.colaborador.delete import exclude_colaborador

router = APIRouter(prefix="/colaborador", tags=["colaborador"])


@router.delete("/matricula/{matricula_colaborador}")
def delete_colaborador(matricula_colaborador: str, db: SessionLocal = Depends(get_db)):
    exclude_colaborador(matricula_colaborador, db)
    return {"message": "Colaborador excluido."}
