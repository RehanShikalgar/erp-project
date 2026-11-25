from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field

class ItemIn(BaseModel):
    description: str =  Field(min_length = 1, max_length= 255)
    quantity: Decimal =  Field(gt = 0)
    unit_price: Decimal = Field(ge=0)

class InvoiceIn(BaseModel):
    invoice_number: str = Field(min_length = 1, max_length = 50)
    vendor_name: str =  Field(min_length=1, max_length = 200)
    invoice_date: date
    stated_total: Decimal | None = None
    items: list[ItemIn] = Field(min_length = 1)