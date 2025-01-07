from fastapi import Depends, APIRouter
from schemas.colaborador import ColaboradorResponse, ColaboradorUpdate, ColaboradorAlterPassword, ColaboradorPromotion
from database.session_db import SessionLocal, get_db
from database.colaborador.update import modify_colaborador, update_promotion, alter_senha, soft_delete_colaborador

router = APIRouter(prefix="/colaborador", tags=["colaborador"])


@router.put("/matricula/{matricula_colaborador}", response_model=ColaboradorResponse)
def update_colaborador(matricula_colaborador: str,
                       colaborador_update: ColaboradorUpdate,
                       db: SessionLocal = Depends(get_db)):
    colaborador = modify_colaborador(matricula_colaborador, colaborador_update, db)
    return colaborador


@router.put("/alterar_senha")
def update_senha(colaborador_alter_password: ColaboradorAlterPassword,
                 db: SessionLocal = Depends(get_db)):

    alter_senha(colaborador_alter_password, db)
    return {"message": "Senha alterada com sucesso"}


@router.put("/{matricula_colaborador}/promover", response_model=ColaboradorResponse)
def promotion_colaborador(matricula_colaborador: str,
                          colaborador_promotion: ColaboradorPromotion,
                          db: SessionLocal = Depends(get_db)):
    colaborador = update_promotion(matricula_colaborador, colaborador_promotion, db)
    return colaborador


@router.put("/{matricula_colaborador}/demitir", response_model=ColaboradorResponse)
def demitir_colaborador(matricula_colaborador: str, db: SessionLocal = Depends(get_db)):
    colaborador = soft_delete_colaborador(matricula_colaborador, db)
    return colaborador
