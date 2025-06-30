import tkinter as tk
from gui.gui_upload import UploadWindow
from gui.gui_invoices import InvoicesWindow
from gui.gui_ratios import RatiosWindow
from gui.gui_reports import ReportsWindow


class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📊 FinanceSight Dashboard")
        self.geometry("600x600")
        self.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="📊 FinanceSight Dashboard", font=("Helvetica", 20, "bold"), fg="#2C3E50", bg="white").pack(pady=20)

        tk.Button(self, text="📤 Upload Invoice", bg="#3498DB", fg="white", width=30,
                  command=self.open_upload).pack(pady=10)

        tk.Button(self, text="📄 View Invoices", bg="#2ECC71", fg="white", width=30,
                  command=self.open_invoices).pack(pady=10)

        tk.Button(self, text="📈 Financial Ratios", bg="#E67E22", fg="white", width=30,
                  command=self.open_ratios).pack(pady=10)

        tk.Button(self, text="📁 Reports Archive", bg="#34495E", fg="white", width=30,
                  command=self.open_archive).pack(pady=10)

        tk.Button(self, text="❌ Exit", bg="#C0392B", fg="white", width=20,
                  command=self.destroy).pack(pady=30)

    def open_upload(self):
        UploadWindow(self)

    def open_invoices(self):
        InvoicesWindow(self)

    def open_ratios(self):
        RatiosWindow(self)

    def open_archive(self):
        ArchiveWindow(self)

if __name__ == "__main__":
    app = DashboardWindow()
    app.mainloop()
