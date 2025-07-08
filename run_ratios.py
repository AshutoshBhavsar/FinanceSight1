import pandas as pd
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os

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

    df['invoice_date'] = pd.to_datetime(df['invoice_date'])
    df['month'] = df['invoice_date'].dt.to_period("M")

    monthly_summary = df.groupby('month').agg(
        total_expense=pd.NamedAgg(column='amount', aggfunc='sum'),
        invoice_count=pd.NamedAgg(column='amount', aggfunc='count')
    ).reset_index()

    cursor = conn.cursor()

    for _, row in monthly_summary.iterrows():
        month = str(row['month'])
        burn_rate = row['total_expense'] / row['invoice_count']

        # Dummy financial values (replace with actual logic)
        current_ratio = 2.5
        quick_ratio = 1.8
        profit_margin = 0.3

        cursor.execute("""
            INSERT INTO ratios (month, current_ratio, quick_ratio, burn_rate, profit_margin)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            current_ratio=VALUES(current_ratio),
            quick_ratio=VALUES(quick_ratio),
            burn_rate=VALUES(burn_rate),
            profit_margin=VALUES(profit_margin)
        """, (month, current_ratio, quick_ratio, burn_rate, profit_margin))

    conn.commit()
    conn.close()
    print("✅ Financial ratios updated.")

if __name__ == "__main__":
    calculate_and_insert_ratios()
