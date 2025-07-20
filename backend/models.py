from pydantic import BaseModel
from typing import Optional
from datetime import date

# Used for receiving data from frontend (e.g. Upload Invoice)
class InvoiceInput(BaseModel):
    vendor: str
    amount: float
    invoice_date: str  # use str if it comes as "2024-07-18"
    category: str
    file_path: str

# Used for sending back response (e.g. showing data)
class InvoiceOutput(BaseModel):
    vendor: str
    amount: float
    invoice_date: date
    category: Optional[str] = "Invoice"
