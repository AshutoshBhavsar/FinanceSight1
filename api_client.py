import requests


BASE_URL = "http://127.0.0.1:8000"
def insert_invoice_api(vendor, amount, date, category, file_path):
    url = "http://127.0.0.1:8000/upload_invoice"
    payload = {
        "vendor": vendor,
        "amount": amount,
        "invoice_date": date,
        "category": category,
        "file_path": file_path
    }
    response = requests.post(url, json=payload)
    return response.ok
def fetch_all_invoices_api():
    url = "http://127.0.0.1:8000/invoices"
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print("API ERROR:", e)
        return []
def fetch_filtered_invoices(vendor="", category="", month=""):
    params = {}
    if vendor:
        params["vendor"] = vendor
    if category:
        params["category"] = category
    if month:
        params["month"] = month

    response = requests.get("http://127.0.0.1:8000/get_invoices", params=params)
    response.raise_for_status()
    return response.json()
def get_latest_ratios_api():
    try:
        res = requests.get("http://127.0.0.1:8000/ratios")
        res.raise_for_status()
        return res.json()
    except:
        return {}
def fetch_latest_ratios():
    response = requests.get("http://127.0.0.1:8000/get_ratios")
    response.raise_for_status()
    return response.json()
def fetch_monthly_expense():
    res = requests.get(f"{BASE_URL}/report/monthly_expenses")
    return res.json() 

def fetch_vendor_expense():
    res = requests.get(f"{BASE_URL}/report/vendor_expenses")
    return res.json()