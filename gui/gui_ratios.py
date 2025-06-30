import tkinter as tk
from tkinter import ttk, messagebox
from api_client import fetch_latest_ratios

class RatiosWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📈 Financial Ratios")
        self.geometry("800x400")
        self.configure(bg="white")

        tk.Label(self, text="📊 Financial Ratios (Last 6 Months)", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Month", "Current Ratio", "Quick Ratio", "Burn Rate", "Profit Margin"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Button(self, text="🔄 Refresh", bg="#3498DB", fg="white", command=self.load_data).pack(pady=10)
        self.load_data()

    def load_data(self):
        try:
            self.tree.delete(*self.tree.get_children())
            rows = fetch_latest_ratios()
            for row in rows:
                self.tree.insert("", "end", values=(
                    row["month"],
                    row["current_ratio"],
                    row["quick_ratio"],
                    row["burn_rate"],
                    row["profit_margin"]
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load ratios:\n{e}")
