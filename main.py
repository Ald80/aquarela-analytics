from fastapi import FastAPI
from routes.colaborador.create import router as colaborador_create_route
from routes.colaborador.delete import router as colaborador_delete_route
from routes.colaborador.update import router as colaborador_update_route
from routes.colaborador.read import router as colaborador_read_route
from exceptions.exception_handlers import conflict_error_handler, not_found_error_handler, server_error_handler
from exceptions.customized_exceptions import ConflictError, NotFoundError, ServerError
from database.session_db import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(colaborador_create_route)
app.include_router(colaborador_delete_route)
app.include_router(colaborador_update_route)
app.include_router(colaborador_read_route)

app.add_exception_handler(ConflictError, conflict_error_handler)
app.add_exception_handler(NotFoundError, not_found_error_handler)
app.add_exception_handler(ServerError, server_error_handler)
