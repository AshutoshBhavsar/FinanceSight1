from fastapi import APIRouter
from backend.db import get_db_connection

router = APIRouter()

@router.get("/ratios")
def get_all_ratios():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT month, current_ratio, quick_ratio, burn_rate, profit_margin 
            FROM ratios ORDER BY month DESC
        """)
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "month": row[0],
                "current_ratio": float(row[1]),
                "quick_ratio": float(row[2]),
                "burn_rate": float(row[3]),
                "profit_margin": float(row[4])
            } for row in rows
        ]
    except Exception as e:
        return {"error": str(e)}
