import requests

API_URL = "http://127.0.0.1:8000"
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
    response = requests.get("http://127.0.0.1:8000/ratios")
    response.raise_for_status()
    return response.json()

def fetch_monthly_expenses():
    try:
        response = requests.get(f"{API_URL}/expenses/monthly")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[API ERROR] fetch_monthly_expenses: {e}")
        return []

def fetch_vendor_expenses():
    try:
        response = requests.get(f"{API_URL}/expenses/by_vendor")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[API ERROR] fetch_vendor_expenses: {e}")
        return []
def fetch_monthly_trends():
    url = "http://127.0.0.1:8000/monthly_trends"
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        raise Exception("API request failed")
def fetch_financial_ratios():
    try:
        response = requests.get("http://127.0.0.1:8000/get_ratios")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("[FETCH RATIOS ERROR]", e)
        return []
    

def fetch_ratios():
    res = requests.get(f"{API_BASE}/get_ratios")
    res.raise_for_status()
    return res.json()
