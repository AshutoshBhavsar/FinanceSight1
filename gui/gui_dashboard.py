import tkinter as tk
from gui.gui_archive import ArchiveWindow
from gui.gui_charts import ChartsWindow
from gui.gui_ratios import RatiosWindow
from gui.gui_reports import ReportsWindow
from gui.gui_upload import UploadWindow

def main():
    root = tk.Tk()
    root.title("📊 FinanceSight - Business Dashboard")
    root.geometry("500x500")
    root.configure(bg="white")

    # Title Label
    title_label = tk.Label(
        root,
        text="📊 FinanceSight - Business Dashboard",
        font=("Segoe UI", 18, "bold"),
        fg="#2C3E50",
        bg="white",
        pady=20
    )
    title_label.pack()

    # Buttons
    btn_style = {
        "font": ("Segoe UI", 12),
        "bg": "#3498DB",
        "fg": "white",
        "activebackground": "#2980B9",
        "activeforeground": "white",
        "width": 25,
        "padx": 10,
        "pady": 10,
        "bd": 0,
        "highlightthickness": 0,
        "cursor": "hand2"
    }

    # Actions
    def open_upload():
        win = UploadWindow()
        win.show()

    def open_reports():
        win = ReportsWindow()
        win.show()

    def open_ratios():
        RatiosWindow(root)

    def open_charts():
        win = ChartsWindow()
        win.show()

    def open_archive():
        win = ArchiveWindow()
        win.show()

    buttons = [
        ("📄 Upload Invoice", open_upload),
        ("💼 View Invoice Table", open_reports),
        ("📊 Financial Ratios", open_ratios),
        ("📊 Charts & Trends", open_charts),
        ("📂 Archived Invoices", open_archive)
    ]

    for text, command in buttons:
        tk.Button(root, text=text, command=command, **btn_style).pack(pady=8)

    root.mainloop()
