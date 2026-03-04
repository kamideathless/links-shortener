from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions.exceptions import NotFoundError


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        return JSONResponse(status_code=404, content={'detail': exc.detail})
