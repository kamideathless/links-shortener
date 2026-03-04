from fastapi import Depends
from pydantic import HttpUrl
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions.exceptions import NotFoundError
from app.db.database import get_session_uow
from app.features.shorter.models.links import Links
from app.features.shorter.schemas import LinkBase, LinkStatsResponse


class LinksService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def increase_clicks(self, shorten_url: str) -> None:
        await self.session.execute(
            update(Links).where(Links.shorten_url == shorten_url).values(total_clicks=Links.total_clicks + 1)
        )

    async def get_original_link(self, shorten_url: str) -> LinkBase:
        original_url = await self.session.scalar(select(Links.original_url).where(Links.shorten_url == shorten_url))
        if not original_url:
            raise NotFoundError(f'Оригинал идентификатора {shorten_url} не найден')
        await self.increase_clicks(shorten_url)
        return LinkBase(original_url=HttpUrl(original_url))

    async def get_link_stats(self, shorten_url: str) -> LinkStatsResponse:
        count = await self.session.scalar(select(Links.total_clicks).where(Links.shorten_url == shorten_url))
        if count is None:
            raise NotFoundError(f'Идентификатор {shorten_url} не найден')
        return LinkStatsResponse(total_clicks=count)

    async def exists(self, shorten_url: str) -> bool:
        url = await self.session.scalar(select(Links.id).where(Links.shorten_url == shorten_url))
        return url is not None


def get_links_service(session: AsyncSession = Depends(get_session_uow)):
    return LinksService(session)
