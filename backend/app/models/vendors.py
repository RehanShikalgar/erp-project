from datetime import datetime, timezone
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    name: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[datetime] =  mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))