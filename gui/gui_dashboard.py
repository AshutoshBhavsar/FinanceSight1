import tkinter as tk
from gui.gui_upload import UploadWindow
from gui.gui_invoices import InvoicesWindow
from gui.gui_ratios import RatiosWindow
from gui.gui_reports import ReportsWindow
from gui.gui_archive import ArchiveWindow
from gui.gui_charts import ChartsWindow
from gui.gui_charts import show_charts
from gui.gui_archive import show_archive

from PyQt6.QtWidgets import QApplication
import sys


class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📊 FinanceSight Dashboard")
        self.geometry("600x600")
        self.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="📊 FinanceSight Dashboard", font=("Helvetica", 20, "bold"), fg="#2C3E50", bg="white").pack(pady=20)

        btn_font = ("Segoe UI", 11, "bold")
        btn_width = 30
        pady = 10

        tk.Button(self, text="📤 Upload Invoice", font=btn_font, width=btn_width,
                  bg="#3498DB", fg="white", command=self.open_upload).pack(pady=pady)

        tk.Button(self, text="📄 View Invoices", font=btn_font, width=btn_width,
                  bg="#2ECC71", fg="white", command=self.open_invoices).pack(pady=pady)

        tk.Button(self, text="📈 Financial Ratios", font=btn_font, width=btn_width,
                  bg="#E67E22", fg="white", command=self.open_ratios).pack(pady=pady)

        tk.Button(self, text="📁 Reports Archive", font=btn_font, width=btn_width,
                  bg="#34495E", fg="white", command=show_archive).pack(pady=pady)

        tk.Button(self, text="📊 Charts & Reports", font=btn_font, width=btn_width,
                  bg="#9B59B6", fg="white", command=show_charts).pack(pady=pady)

        tk.Button(self, text="❌ Exit", font=btn_font, width=20,
                  bg="#C0392B", fg="white", command=self.destroy).pack(pady=30)

    def open_upload(self):
        UploadWindow(self)

    def open_invoices(self):
        InvoicesWindow(self)

    def open_ratios(self):
        RatiosWindow(self)

    def open_archive(self):
        ArchiveWindow(self)
    
    def safe_launch_pyqt(window_class):
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)
        win = window_class()
        win.show()
if __name__ == "__main__":
    app = DashboardWindow()
    app.mainloop()
