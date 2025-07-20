import tkinter as tk
from gui.gui_upload import UploadWindow
from gui.gui_invoices import InvoicesWindow
from gui.gui_ratios import RatiosWindow
from gui.gui_reports import ReportsWindow
from gui.gui_archive import ArchiveWindow
from gui.gui_charts import ChartsWindow
from PyQt6.QtWidgets import QApplication
from gui.gui_charts import ChartsWindow
import sys

class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📊 FinanceSight Dashboard")
        self.state('zoomed')  # Full screen
        self.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="📊 FinanceSight Dashboard", font=("Helvetica", 24, "bold"), fg="#2C3E50", bg="white").pack(pady=40)

        btn_font = ("Segoe UI", 12, "bold")
        btn_width = 30
        pady = 12

        tk.Button(self, text="📤 Upload Invoice", bg="#3498DB", fg="white", width=btn_width,
                  font=btn_font, command=self.open_upload).pack(pady=pady)

        tk.Button(self, text="📄 View Invoices", bg="#2ECC71", fg="white", width=btn_width,
                  font=btn_font, command=self.open_invoices).pack(pady=pady)

        tk.Button(self, text="📈 Financial Ratios", bg="#E67E22", fg="white", width=btn_width,
                  font=btn_font, command=self.open_ratios).pack(pady=pady)

        tk.Button(self, text="📁 Reports Archive", bg="#34495E", fg="white", width=btn_width,
                  font=btn_font, command=self.open_archive).pack(pady=pady)

        tk.Button(self, text="📊 Charts & Reports", bg="#9B59B6", fg="white", width=btn_width,
                  font=btn_font, command=self.show_charts).pack(pady=pady)

        tk.Button(self, text="❌ Exit", bg="#C0392B", fg="white", width=20,
                  font=btn_font, command=self.destroy).pack(pady=30)

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
        from PyQt6.QtWidgets import QApplication
        import sys

        if not hasattr(self, 'qt_app') or self.qt_app is None:
            self.qt_app = QApplication.instance() or QApplication(sys.argv)

        self.qt_window = window_class()
        self.qt_window.show()


if __name__ == "__main__":
    app = DashboardWindow()
    app.mainloop()
