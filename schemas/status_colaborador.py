from pydantic import BaseModel, ConfigDict

class StatusColaboradorBase(BaseModel):
    # id = int
    nome: str
    cd_status: str

class StatusColaboradorCreate(StatusColaboradorBase):
    # id = int
    pass

class StatusColaboradorResponse(StatusColaboradorBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)

