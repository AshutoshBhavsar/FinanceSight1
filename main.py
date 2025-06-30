import tkinter as tk
from gui.gui_upload import UploadWindow
from gui.gui_invoices import InvoicesWindow
from gui.gui_ratios import RatiosWindow
from gui.gui_reports import ReportsWindow
from gui.gui_dashboard import DashboardWindow

class DashboardWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("📊 FinanceSight Dashboard")
        parent.geometry("500x500")
        parent.configure(bg="#F8F9FA")
        self.configure(bg="#F8F9FA")
        self.pack(padx=30, pady=30)

        tk.Label(self, text="📊 FinanceSight Dashboard", font=("Segoe UI", 20, "bold"), fg="#2C3E50", bg="#F8F9FA").pack(pady=20)

        # Button style
        btn_font = ("Segoe UI", 11, "bold")
        btn_width = 25
        pady = 10

        tk.Button(self, text="📤 Upload Invoice PDF", font=btn_font, width=btn_width,
                  bg="#3498DB", fg="white", command=lambda: UploadWindow(parent)).pack(pady=pady)

        tk.Button(self, text="📄 View Invoices Table", font=btn_font, width=btn_width,
                  bg="#2ECC71", fg="white", command=lambda: InvoicesWindow(parent)).pack(pady=pady)

        tk.Button(self, text="📈 Financial Ratios", font=btn_font, width=btn_width,
                  bg="#E67E22", fg="white", command=lambda: RatiosWindow(parent)).pack(pady=pady)

        tk.Button(self, text="📊 Charts & Reports", font=btn_font, width=btn_width,
                  bg="#9B59B6", fg="white", command=lambda: ReportsWindow(parent)).pack(pady=pady)

        tk.Button(self, text="❌ Exit", font=btn_font, width=20,
                  bg="#C0392B", fg="white", command=parent.quit).pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardWindow(root)
    root.mainloop()
