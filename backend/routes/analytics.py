from fastapi import APIRouter
from backend.db import get_db_connection

router = APIRouter()

@router.get("/chart/monthly_expense")
def get_monthly_expense():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DATE_FORMAT(invoice_date, '%Y-%m') as month, SUM(amount)
            FROM invoices
            GROUP BY month
            ORDER BY month
        """)
        data = cursor.fetchall()
        conn.close()

        return [
            {"month": row[0], "total": float(row[1] or 0)}
            for row in data
        ]
    except Exception as e:
        print("🔥 ERROR in /chart/monthly_expense:", e)
        return {"error": str(e)}
