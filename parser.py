import re
from datetime import datetime

def parse_invoice_data(text):
    vendor = None
    amount = None
    date = None

    lines = [line.strip() for line in text.split('\n') if line.strip()]

    # 1. Extract Vendor (look for "Vendor:" line)
    for line in lines:
        if line.lower().startswith("vendor:"):
            vendor = line.split(":", 1)[1].strip()
            break

    # 2. Extract Amount (₹12,500 or ₹12,500.00)
    amount_match = re.search(r"(₹|\$)?\s?([\d,]+(?:\.\d{2})?)", text)
    if amount_match:
        try:
            amount = float(amount_match.group(2).replace(",", ""))
        except:
            amount = None

    # 3. Extract Date (from 'Date:' line)
    date_match = re.search(r"Date:\s*(\d{4}-\d{2}-\d{2})", text)
    if date_match:
        try:
            date = datetime.strptime(date_match.group(1), "%Y-%m-%d").date()
        except:
            date = None

    return vendor, amount, date, text
