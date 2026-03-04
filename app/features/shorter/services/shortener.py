import secrets
import string

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.settings import settings
from app.db.database import get_session_uow
from app.features.shorter.models.links import Links
from app.features.shorter.schemas import ShortLinkCreate, ShortLinkResponse
from app.features.shorter.services.links import LinksService


class ShortenerService:
    def __init__(self, session: AsyncSession, links_service: LinksService):
        self.session = session
        self.links_service = links_service

    @staticmethod
    def _generate_short_id(short_length: int = settings.SHORT_LINK_LENGTH) -> str:
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(short_length))

    async def generate_short_link(self, payload: ShortLinkCreate) -> ShortLinkResponse:
        while True:
            shorten_url = self._generate_short_id()
            if not await self.links_service.exists(shorten_url):
                break

        link = Links(original_url=str(payload.original_url), shorten_url=shorten_url)
        self.session.add(link)
        await self.session.flush()
        return ShortLinkResponse(shorten_link=shorten_url)


def get_shortener_service(session: AsyncSession = Depends(get_session_uow)):
    return ShortenerService(session, links_service=LinksService(session))
