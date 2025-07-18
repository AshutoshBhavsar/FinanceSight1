from fastapi import APIRouter, Query
from backend.models import Invoice
from backend.db import get_db_connection
from typing import Optional

router = APIRouter()

# 1. Upload invoice
@router.post("/upload_invoice")
def upload_invoice(data: Invoice):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO invoices (vendor, amount, invoice_date, category, file_path)
            VALUES (%s, %s, %s, %s, %s)
        """, (data.vendor, data.amount, data.invoice_date, data.category, data.file_path))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Invoice inserted"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# 2. Get invoices with filters
@router.get("/get_invoices")
def get_invoices(
    vendor: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    month: Optional[str] = Query(None)  # Format: YYYY-MM
):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT vendor, amount, invoice_date, category , file_path FROM invoices WHERE 1=1"
        params = []

        if vendor:
            query += " AND vendor LIKE %s"
            params.append(f"%{vendor}%")
        if category:
            query += " AND category = %s"
            params.append(category)
        if month:
            query += " AND DATE_FORMAT(invoice_date, '%%Y-%%m') = %s"
            params.append(month)

        query += " ORDER BY invoice_date DESC"
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        conn.close()

        return [
            {"vendor": r[0], "amount": float(r[1]), "invoice_date": str(r[2]), "category": r[3], "file_path": r[4]}
            for r in rows
        ]
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/invoices/archive")
def get_invoice_archive():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT vendor, amount, invoice_date, category, file_path 
            FROM invoices ORDER BY invoice_date DESC
        """)
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "vendor": r[0],
                "amount": float(r[1]),
                "invoice_date": str(r[2]),
                "category": r[3],
                "file_path": r[4]
            }
            for r in rows
        ]
    except Exception as e:
        return {"error": str(e)}


@router.get("/get_archive")
def get_archive():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT vendor, amount, invoice_date, category, file_path FROM invoices ORDER BY invoice_date DESC")
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                "vendor": r[0],
                "amount": float(r[1]),
                "invoice_date": str(r[2]),
                "category": r[3],
                "file_path": r[4]
            }
            for r in rows
        ]
    except Exception as e:
        return {"error": str(e)}
