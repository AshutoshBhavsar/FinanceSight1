import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
from api_client import fetch_filtered_invoices  # Ensure this fetches file_path too!

class ArchiveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📁 Reports Archive")
        self.geometry("950x500")
        self.configure(bg="white")

        tk.Label(self, text="📁 All Uploaded Files", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        # Filters
        filter_frame = tk.Frame(self, bg="white")
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Vendor:", bg="white").grid(row=0, column=0, padx=5)
        self.vendor_entry = tk.Entry(filter_frame)
        self.vendor_entry.grid(row=0, column=1, padx=5)

        tk.Label(filter_frame, text="Category:", bg="white").grid(row=0, column=2, padx=5)
        self.category_cb = ttk.Combobox(filter_frame, values=["", "Invoice", "Profit & Loss Statement", "Expense Report"], state="readonly")
        self.category_cb.grid(row=0, column=3, padx=5)

        tk.Label(filter_frame, text="Month (YYYY-MM):", bg="white").grid(row=0, column=4, padx=5)
        self.month_entry = tk.Entry(filter_frame)
        self.month_entry.grid(row=0, column=5, padx=5)

        tk.Button(filter_frame, text="🔍 Filter", command=self.load_data, bg="#3498DB", fg="white").grid(row=0, column=6, padx=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("Vendor", "Amount", "Date", "Category", "File Path"), show="headings")
        for col in ("Vendor", "Amount", "Date", "Category", "File Path"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180 if col != "Amount" else 100)

        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Open file
        tk.Button(self, text="📂 Open Selected File", command=self.open_selected_file, bg="#2ECC71", fg="white").pack(pady=5)
        tk.Button(self, text="🔄 Clear Filters", command=self.clear_filters).pack(pady=5)

        self.load_data()

    def load_data(self):
        vendor = self.vendor_entry.get()
        category = self.category_cb.get()
        month = self.month_entry.get()

        try:
            self.tree.delete(*self.tree.get_children())
            data = fetch_filtered_invoices(vendor, category, month)
            for row in data:
                self.tree.insert("", "end", values=(row["vendor"], row["amount"], row["invoice_date"], row["category"], row["file_path"]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data:\n{e}")

    def clear_filters(self):
        self.vendor_entry.delete(0, tk.END)
        self.category_cb.set("")
        self.month_entry.delete(0, tk.END)
        self.load_data()

    def open_selected_file(self):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            file_path = values[4]
            if os.path.exists(file_path):
                try:
                    os.startfile(file_path)  # Windows only
                except:
                    subprocess.call(["open", file_path])  # macOS/Linux
            else:
                messagebox.showerror("File Missing", "The selected file no longer exists.")
        else:
            messagebox.showinfo("No Selection", "Please select a row to open the file.")
