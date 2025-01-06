from pydantic import BaseModel, ConfigDict
class LiderBase(BaseModel):
    # id = int
    nome: str
    matricula: str
class LiderCreate(LiderBase):
    pass
class LiderResponse(LiderBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

