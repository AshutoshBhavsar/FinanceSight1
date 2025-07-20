import tkinter as tk
from gui.gui_upload import UploadWindow
from gui.gui_invoices import InvoicesWindow
from gui.gui_ratios import RatiosWindow
from gui.gui_reports import ReportsWindow
from gui.gui_archive import ArchiveWindow
from gui.gui_charts import ChartsWindow
from PyQt6.QtWidgets import QApplication
import sys

class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📊 FinanceSight Dashboard")
        self.state('zoomed')
        self.configure(bg="#121212")  # Dark mode background
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="📊 FinanceSight Dashboard", font=("Helvetica", 24, "bold"), fg="#EAEAEA", bg="#121212").pack(pady=40)

        btn_font = ("Segoe UI", 12, "bold")
        btn_width = 30
        pady = 12

        style_config = {
            "font": btn_font,
            "fg": "#FFFFFF",
            "activeforeground": "#000",
        }

        tk.Button(self, text="📤 Upload Invoice", bg="#1E88E5", width=btn_width, **style_config, command=self.open_upload).pack(pady=pady)
        tk.Button(self, text="📄 View Invoices", bg="#43A047", width=btn_width, **style_config, command=self.open_invoices).pack(pady=pady)
        tk.Button(self, text="📈 Financial Ratios", bg="#FB8C00", width=btn_width, **style_config, command=self.open_ratios).pack(pady=pady)
        tk.Button(self, text="📁 Reports Archive", bg="#37474F", width=btn_width, **style_config, command=self.open_archive).pack(pady=pady)
        tk.Button(self, text="📊 Charts & Reports", bg="#8E24AA", width=btn_width, **style_config, command=self.show_charts).pack(pady=pady)
        tk.Button(self, text="❌ Exit", bg="#D32F2F", width=20, **style_config, command=self.destroy).pack(pady=30)

    def open_upload(self):
        UploadWindow(self)

    def open_invoices(self):
        InvoicesWindow(self)

    def open_ratios(self):
        RatiosWindow(self)

    def open_archive(self):
        self.launch_qt_window(ArchiveWindow)

    def show_charts(self):
        self.launch_qt_window(ChartsWindow)

    def open_charts():
        ChartsWindow().show()

    def launch_qt_window(self, window_class):
        if not hasattr(self, 'qt_app') or self.qt_app is None:
            self.qt_app = QApplication.instance() or QApplication(sys.argv)
        self.qt_window = window_class()
        self.qt_window.show()

if __name__ == "__main__":
    app = DashboardWindow()
    app.mainloop()
