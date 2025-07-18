from fastapi import APIRouter
from backend.db import get_db_connection

router = APIRouter()

@router.get("/monthly_trends")
def monthly_trends():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DATE_FORMAT(invoice_date, '%Y-%m') as month, SUM(amount)
            FROM invoices
            GROUP BY month ORDER BY month
        """)
        rows = cursor.fetchall()
        conn.close()
        return [{"month": r[0], "total": float(r[1])} for r in rows]
    except Exception as e:
        return {"error": str(e)}
