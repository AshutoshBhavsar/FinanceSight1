from fastapi import APIRouter
from backend.db import get_db_connection

router = APIRouter()

# ✅ Fixed: monthly_expense chart
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
    return [{"month": row[0], "total": float(row[1])} for row in data]  # ✅ fixed

# ✅ Fixed: vendor_expense chart
@router.get("/chart/vendor_expense")
def get_vendor_expense():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT vendor, SUM(amount) FROM invoices GROUP BY vendor")
    data = cursor.fetchall()
    conn.close()
    return [{"vendor": row[0], "total": float(row[1])} for row in data]  # ✅ fixed

# ✅ Valid: monthly trends
@router.get("/monthly_trends")
def monthly_trends():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE_FORMAT(invoice_date, '%Y-%m') AS month, SUM(amount) AS total 
        FROM invoices 
        GROUP BY month 
        ORDER BY month
    """)
    rows = cursor.fetchall()
    conn.close()
    return [{"month": r[0], "total": float(r[1])} for r in rows]

# ✅ Optional: remove or implement these
@router.get("/expenses/monthly")
def get_monthly_expenses():
    # Optional logic (can be removed if unused)
    return {"message": "Not implemented"}

@router.get("/expenses/by_vendor")
def get_expenses_by_vendor():
    # Optional logic (can be removed if unused)
    return {"message": "Not implemented"}
