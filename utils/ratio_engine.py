import mysql.connector
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def calculate_and_insert_ratios():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    df = pd.read_sql("SELECT * FROM invoices", conn)

    if df.empty:
        print("No invoices found.")
        return

    month = datetime.today().strftime("%Y-%m")

    total_expenses = df["amount"].sum()
    burn_rate = total_expenses / len(df["invoice_date"].unique())

    # Static or mocked values for now
    current_ratio = 1.8
    quick_ratio = 1.5
    profit_margin = 0.25  # or based on revenue if you have it

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ratios (month, current_ratio, quick_ratio, burn_rate, profit_margin)
        VALUES (%s, %s, %s, %s, %s)
    """, (month, current_ratio, quick_ratio, burn_rate, profit_margin))

    conn.commit()
    conn.close()
    print("✅ Ratios inserted.")
