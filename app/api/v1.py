from fastapi import APIRouter

from app.features.shorter.api import shortener_router

router = APIRouter(prefix='/api/v1')

router.include_router(shortener_router)
