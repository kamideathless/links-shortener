from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Links(Base):
    __tablename__ = 'links'

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column()
    shorten_url: Mapped[str] = mapped_column(unique=True, index=True)
    total_clicks: Mapped[int] = mapped_column(default=0)
