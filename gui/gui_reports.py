import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests

class ReportsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("📊 Charts & Reports")
        self.geometry("800x600")
        self.configure(bg="white")

        tk.Label(self, text="📊 Financial Charts & Trends", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

        tk.Button(self, text="📅 Monthly Expense Trend", bg="#2980B9", fg="white", command=self.plot_monthly_trend).pack(pady=10)
        tk.Button(self, text="🏢 Vendor Wise Spend", bg="#27AE60", fg="white", command=self.plot_vendor_distribution).pack(pady=10)

        self.canvas_frame = tk.Frame(self, bg="white")
        self.canvas_frame.pack(pady=20, fill="both", expand=True)

    def plot_monthly_trend(self):
        try:
            res = requests.get("http://127.0.0.1:8000/chart/monthly_expense")
            data = res.json()

            months = [item["month"] for item in data]
            totals = [item["total"] for item in data]

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(months, totals, marker='o', color='blue')
            ax.set_title("Monthly Expenses")
            ax.set_ylabel("Total Amount (₹)")
            ax.set_xlabel("Month")
            ax.grid(True)

            self.render_chart(fig)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data:\n{e}")

    def plot_vendor_distribution(self):
        try:
            res = requests.get("http://127.0.0.1:8000/chart/vendor_expense")
            data = res.json()

            vendors = [item["vendor"] for item in data]
            totals = [item["total"] for item in data]

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(vendors, totals, color='green')
            ax.set_title("Vendor-wise Spend")
            ax.set_ylabel("Total Amount (₹)")
            ax.set_xlabel("Vendor")
            ax.tick_params(axis='x', rotation=45)

            self.render_chart(fig)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data:\n{e}")

    def render_chart(self, fig):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
