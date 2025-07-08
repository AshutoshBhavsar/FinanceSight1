from fastapi import APIRouter
from backend.db import get_db_connection

router = APIRouter()

@router.get("/chart/monthly_expense")
def get_monthly_expense():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE_FORMAT(invoice_date, '%Y-%m') as month, SUM(amount)
        FROM invoices GROUP BY month ORDER BY month
    """)
    data = cursor.fetchall()
    conn.close()
    return [{"month": row[0], "total": float(row[1])} for row in rows]

@router.get("/chart/vendor_expense")
def get_vendor_expense():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT vendor, SUM(amount) FROM invoices GROUP BY vendor")
    data = cursor.fetchall()
    conn.close()
    return [{"vendor": row[0], "total": float(row[1])} for row in rows]
