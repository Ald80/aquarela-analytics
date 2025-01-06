from pydantic import BaseModel, ConfigDict
class CargoBase(BaseModel):
    # id = str
    nome: str
    cd_codigo: str
    salario: float

class CargoCreate(CargoBase): 
    pass
class CargoResponse(CargoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

