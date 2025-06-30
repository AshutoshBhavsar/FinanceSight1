import tkinter as tk
from tkinter import ttk, messagebox
from api_client import fetch_filtered_invoices

class InvoicesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📄 View Invoices Table")
        self.geometry("900x500")
        self.configure(bg="white")

        # Title
        tk.Label(self, text="📄 Uploaded Invoices", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # Filters
        filter_frame = tk.Frame(self, bg="white")
        filter_frame.pack(pady=10)

        tk.Label(filter_frame, text="Vendor:", bg="white").grid(row=0, column=0, padx=5)
        self.vendor_entry = tk.Entry(filter_frame)
        self.vendor_entry.grid(row=0, column=1, padx=5)

        tk.Label(filter_frame, text="Category:", bg="white").grid(row=0, column=2, padx=5)
        self.category_cb = ttk.Combobox(filter_frame, values=["", "Invoice", "Profit & Loss Statement", "Expense Report"], state="readonly")
        self.category_cb.grid(row=0, column=3, padx=5)

        tk.Label(filter_frame, text="Month (YYYY-MM):", bg="white").grid(row=0, column=4, padx=5)
        self.month_entry = tk.Entry(filter_frame)
        self.month_entry.grid(row=0, column=5, padx=5)

        tk.Button(filter_frame, text="🔍 Apply Filters", bg="#3498DB", fg="white", command=self.load_data).grid(row=0, column=6, padx=10)

        # TreeView
        self.tree = ttk.Treeview(self, columns=("Vendor", "Amount", "Date", "Category"), show="headings")
        for col in ("Vendor", "Amount", "Date", "Category"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150 if col != "Amount" else 100)

        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        # Refresh
        tk.Button(self, text="🔄 Clear Filters", bg="#2ECC71", fg="white", command=self.clear_filters).pack(pady=5)

        self.load_data()

    def load_data(self):
        vendor = self.vendor_entry.get()
        category = self.category_cb.get()
        month = self.month_entry.get()

        try:
            self.tree.delete(*self.tree.get_children())
            rows = fetch_filtered_invoices(vendor, category, month)
            for row in rows:
                self.tree.insert("", "end", values=(row["vendor"], row["amount"], row["invoice_date"], row["category"]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load invoices:\n{e}")

    def clear_filters(self):
        self.vendor_entry.delete(0, tk.END)
        self.category_cb.set("")
        self.month_entry.delete(0, tk.END)
        self.load_data()
