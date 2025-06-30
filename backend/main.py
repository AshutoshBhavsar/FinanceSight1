from fastapi import FastAPI
from backend.routes import invoices, ratios
from backend.routes import reports
from backend.routes import archive


app = FastAPI()

app.include_router(invoices.router)
app.include_router(ratios.router)
app.include_router(reports.router)
app.include_router(archive.router)