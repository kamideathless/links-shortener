from pydantic import BaseModel, HttpUrl


class LinkBase(BaseModel):
    original_url: HttpUrl


class ShortLinkCreate(LinkBase):
    pass


class ShortLinkResponse(BaseModel):
    shorten_link: str


class LinkStatsResponse(BaseModel):
    total_clicks: int
