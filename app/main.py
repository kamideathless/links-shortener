from fastapi import FastAPI

from app.api.v1 import router as v1_router
from app.core.exceptions.handlers import register_exception_handlers

app = FastAPI()

app.include_router(v1_router)

register_exception_handlers(app)
