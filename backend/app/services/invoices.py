from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Invoice, InvoiceItem, User, Vendor
from app.schemas.invoices import InvoiceIn

def get_or_create_vendor(db: Session, user: User, name: str) -> Vendor:
    vendor = db.scalar(select(Vendor).where(Vendor.user_id==user.id, Vendor.name == name))

    if vendor is None:
        vendor = Vendor(user_id = user.id, name = name)
        db.add(vendor)
        db.flush()
    return vendor

def save_invoice(db: Session, user: User, data: InvoiceIn) -> Invoice:
    vendor = get_or_create_vendor(db, user, data.vendor_name.strip())
    computed = sum(i.quantity * i.unit_price for i in data.items)

    invoice = Invoice(user_id = user.id, vendor_id = vendor.id, invoice_number = data.invoice_number.strip(), invoice_date=data.invoice_date, total = data.stated_total if data.stated_total is not None else computed)
    db.add(invoice)
    db.flush()
    db.add_all(InvoiceItem(invoice_id = invoice.id, description=i.description, quantity = i.quantity, unit_price=i.unit_price)for i in data.items)

    db.commit()
    return invoice