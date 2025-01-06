from pydantic import BaseModel, ConfigDict
from typing import Optional
from .cargo import CargoResponse
from .lider import LiderResponse
from .status_colaborador import StatusColaboradorResponse

class ColaboradorCreate(BaseModel):
    nome: str
    sobrenome: str
    matricula: str
    senha: str
    id_cargo: int
    id_status: int
    id_lider: int

class ColaboradorUpdate(BaseModel):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    senha: Optional[str] = None
    id_cargo: Optional[int] = None
    id_status: Optional[int] = None
    id_lider: Optional[int] = None

class ColaboradorAlterPassword(BaseModel):
    matricula: str
    senha: str

class ColaboradorPromotion(BaseModel):
    id_cargo: int
    id_lider: Optional[int] = None

class ColaboradorResponse(BaseModel):
    id: int
    nome: str
    sobrenome: str
    matricula: str
    cargo: CargoResponse
    lider: LiderResponse
    status: StatusColaboradorResponse

    model_config = ConfigDict(from_attributes=True)