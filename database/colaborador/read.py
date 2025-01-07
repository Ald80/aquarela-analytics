from sqlalchemy.orm import Session
from models.colaborador import Colaborador as ColaboradorModel
from models.status_colaborador import StatusColaborador as StatusColaboradorModel
from models.status_colaborador import StatusColaborador as StatusColaboradorModel


def fetch_all_colaboradores(db: Session):
    return db.query(ColaboradorModel).all()


def fetch_colaborador_by_matricula(matricula_colaborador: str, db: Session):
    return db.query(ColaboradorModel).filter(
        ColaboradorModel.matricula == matricula_colaborador).first()


def fetch_status_colaborador_by_id(id_status_colaborador: int, db: Session):
    return db.query(StatusColaboradorModel).filter(
        StatusColaboradorModel.id == id_status_colaborador).first()
