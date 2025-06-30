from pydantic import BaseModel
from typing import Optional
from datetime import date
from pydantic import BaseModel


class Invoice(BaseModel):
    vendor: str
    amount: float
    invoice_date: date
    category: Optional[str] = "Invoice"
class Invoice(BaseModel):
    vendor: str
    amount: float
    invoice_date: str
    category: str
    file_path: str  