from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from app.features.shorter.schemas import LinkBase, LinkStatsResponse, ShortLinkCreate, ShortLinkResponse
from app.features.shorter.services.links import LinksService, get_links_service
from app.features.shorter.services.shortener import ShortenerService, get_shortener_service

router = APIRouter(tags=['Ссылки'])


@router.post('/shorten', response_model=ShortLinkResponse)
async def shorten_link(payload: ShortLinkCreate, service: ShortenerService = Depends(get_shortener_service)):
    return await service.generate_short_link(payload)


@router.get('/stats/{short_id}', response_model=LinkStatsResponse)
async def get_clicks_count(short_id: str, service: LinksService = Depends(get_links_service)):
    return await service.get_link_stats(short_id)


@router.get('/{short_id}')
async def get_original_link(short_id: str, service: LinksService = Depends(get_links_service)) -> RedirectResponse:
    link = await service.get_original_link(short_id)
    return RedirectResponse(url=str(link.original_url))
