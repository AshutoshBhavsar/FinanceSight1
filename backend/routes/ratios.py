from fastapi import APIRouter
from backend.db import get_db_connection

router = APIRouter()

@router.get("/get_ratios")
def get_latest_ratios():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT month, current_ratio, quick_ratio, burn_rate, profit_margin
        FROM ratios
        ORDER BY month DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()

    print("DEBUG - Latest Ratio Row:", row)  # ✅ Always show what's fetched

    if row:
        return {
            "month": row[0],
            "current_ratio": row[1],
            "quick_ratio": row[2],
            "burn_rate": row[3],
            "profit_margin": row[4]
        }
    else:
        return {"message": "No financial ratios found"}
@router.get("/get_all_ratios")
def get_all_ratios():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT month, current_ratio, quick_ratio, burn_rate, profit_margin
        FROM ratios
        ORDER BY month DESC
        LIMIT 6
    """)
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "month": row[0],
            "current_ratio": row[1],
            "quick_ratio": row[2],
            "burn_rate": row[3],
            "profit_margin": row[4]
        }
        for row in rows
    ]
