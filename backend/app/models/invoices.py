from datetime import datetime, timezone, date
from decimal import Decimal
from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)

    #_____________________________________________________________________
    # Repeated on purpose. We could find the owner through the vendor,
    # but "show all invoices of this user" is the most common search,
    # so we store the owner here too and skip the extra step.
    # Rule: this must always match the vendor's user_id.
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    #____________________________________________________________________

    vendor_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))
    invoice_number: Mapped[str] = mapped_column(String(50), index=True)
    invoice_date: Mapped[date] = mapped_column(Date)
    total: Mapped[Decimal] = mapped_column(Numeric(12,2))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default = lambda: datetime.now(timezone.utc))
