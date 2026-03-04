from unittest.mock import AsyncMock

import pytest

from app.core.exceptions.exceptions import NotFoundError
from app.features.shorter.services.links import LinksService


@pytest.mark.asyncio
async def test_get_original_link_raises_not_found():
    session = AsyncMock()
    session.scalar.return_value = None

    service = LinksService(session)

    with pytest.raises(NotFoundError):
        await service.get_original_link('abc123')


@pytest.mark.asyncio
async def test_increase_clicks_on_get_original_link():
    session = AsyncMock()
    session.scalar.return_value = 'https://example.com'

    service = LinksService(session)
    await service.get_original_link('abc123')

    session.execute.assert_called_once()
