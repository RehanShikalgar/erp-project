from datetime import datetime, timezone
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class anomalyAlert(Base):
    __tablename__ = "anomaly_alerts"

    id: Mapped[int] = mapped_column(primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id", ondelete="CASCADE"))
    rule: Mapped[str] = mapped_column(String(50))
    severity: Mapped[str]= mapped_column(String(20))
    message: Mapped[str] = mapped_column(String(255))
    is_reviewed: Mapped[bool] = mapped_column(Boolean, default=False)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, default=None)
    created_at: Mapped[datetime] = mapped_column(DateTime, default = lambda: datetime.now(timezone.utc))