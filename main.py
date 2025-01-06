from fastapi import FastAPI
from routes.colaborador.create import router  as colaborador_create_route 
from routes.colaborador.delete import router as colaborador_delete_route 
from routes.colaborador.update import router as colaborador_update_route 
from routes.colaborador.read import router as colaborador_read_route 

app = FastAPI()
app.include_router(colaborador_create_route)
app.include_router(colaborador_delete_route)
app.include_router(colaborador_update_route)
app.include_router(colaborador_read_route)
