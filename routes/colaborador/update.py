from fastapi import FastAPI, Depends, APIRouter, HTTPException, Response
from schemas.colaborador import ColaboradorResponse, ColaboradorUpdate, ColaboradorCreate, ColaboradorAlterPassword, ColaboradorPromotion
from database.session_db import SessionLocal, get_db
from database.colaborador.update import modify_colaborador, update_promotion, alter_senha, soft_delete_colaborador
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus
from exceptions.customized_exceptions import ServerError, NotFoundError, ConflictError

router = APIRouter(prefix="/colaborador", tags=["colaborador"])

@router.put("/matricula/{matricula_colaborador}", response_model=ColaboradorResponse)
def update_colaborador(matricula_colaborador: str, colaborador_update: ColaboradorUpdate ,db: SessionLocal = Depends(get_db)):
    try:
        colaborador = modify_colaborador(matricula_colaborador, colaborador_update, db)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f"{e}")
    return colaborador

@router.put("/alterar_senha")
def update_senha(colaborador_alter_password: ColaboradorAlterPassword, db: SessionLocal = Depends(get_db)):
    try:
        alter_senha(colaborador_alter_password, db)
        return {"message": "Senha alterada com sucesso"}
    except NotFoundError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=e.message)
    except ServerError as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=e.message)
    
@router.put("/{matricula_colaborador}/promover", response_model=ColaboradorResponse)
def promotion_colaborador(matricula_colaborador: str, colaborador_promotion: ColaboradorPromotion ,db: SessionLocal = Depends(get_db)):
    try:
        colaborador = update_promotion(matricula_colaborador, colaborador_promotion, db)
        return colaborador
    except NotFoundError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=e.message)
    except ConflictError as e:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=e.message)
    except ServerError as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=e.message)
    
@router.put("/{matricula_colaborador}/demitir", response_model=ColaboradorResponse)
def demitir_colaborador(matricula_colaborador: str, db: SessionLocal = Depends(get_db)):
    try:
        colaborador = soft_delete_colaborador(matricula_colaborador, db)
        return colaborador
    except NotFoundError as e:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=e.message)
    except ConflictError as e:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=e.message)
    except ServerError as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=e.message)