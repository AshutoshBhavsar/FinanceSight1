import tkinter as tk
from tkinter import ttk, messagebox
from api_client import fetch_all_ratios

class RatiosWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📈 Financial Ratios")
        self.geometry("800x400")
        self.configure(bg="white")

        tk.Label(self, text="📊 Financial Ratios (Last 6 Months)", font=("Segoe UI", 16, "bold"), fg="#2C3E50", bg="white").pack(pady=10)

        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))

        self.tree = ttk.Treeview(self, columns=("Month", "Current Ratio", "Quick Ratio", "Burn Rate", "Profit Margin"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130, anchor=tk.CENTER)
        self.tree.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Button(self, text="🔄 Refresh", bg="#3498DB", fg="white", font=("Segoe UI", 11, "bold"), command=self.load_data).pack(pady=10)

        self.load_data()

    def load_data(self):
        try:
            self.tree.delete(*self.tree.get_children())
            data_list = fetch_all_ratios()

            if not data_list:
                raise ValueError("No financial ratio data available.")

            for data in data_list:
                self.tree.insert("", "end", values=(
                    data.get("month", "N/A"),
                    data.get("current_ratio", "-"),
                    data.get("quick_ratio", "-"),
                    data.get("burn_rate", "-"),
                    data.get("profit_margin", "-")
                ))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load ratios:\n{e}")
