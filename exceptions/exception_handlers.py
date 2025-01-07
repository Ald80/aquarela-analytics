from fastapi import Request
from fastapi.responses import JSONResponse
from http import HTTPStatus
from .customized_exceptions import ConflictError, NotFoundError, ServerError


async def not_found_error_handler(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND,
                        content={"detail": exc.message})


async def server_error_handler(request: Request, exc: ServerError):
    return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                        content={"detail": exc.message})


async def conflict_error_handler(request: Request, exc: ConflictError):
    return JSONResponse(status_code=HTTPStatus.CONFLICT,
                        content={"detail": exc.message})
