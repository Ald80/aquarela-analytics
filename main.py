from fastapi import FastAPI
from routes import colaborador


app = FastAPI()
app.include_router(colaborador.router)

# api_router = APIRouter()
# api_router.include_router(colaborador.router)
# api_router.include_router()