from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTabWidget, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from api_client import fetch_monthly_expenses, fetch_vendor_expenses

class ReportsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Charts & Reports")
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()
        title = QLabel("📊 Financial Charts & Reports")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        tabs = QTabWidget()
        tabs.addTab(self.monthly_expense_tab(), "📅 Monthly Expenses")
        tabs.addTab(self.vendor_expense_tab(), "🏢 Vendor Wise")
        layout.addWidget(tabs)

        self.setLayout(layout)

    def monthly_expense_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        try:
            data = fetch_monthly_expenses()
            months = [row["month"] for row in data]
            totals = [row["total"] for row in data]

            fig = Figure(figsize=(5, 4))
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)
            ax.bar(months, totals, color="#3498DB")
            ax.set_title("Monthly Expenses")
            ax.set_ylabel("Amount (₹)")
            ax.set_xlabel("Month")
            fig.tight_layout()
            layout.addWidget(canvas)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load monthly expenses:\n{e}")

        widget.setLayout(layout)
        return widget

    def vendor_expense_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        try:
            data = fetch_vendor_expenses()
            vendors = [row["vendor"] for row in data]
            totals = [row["total"] for row in data]

            fig = Figure(figsize=(5, 4))
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)
            ax.pie(totals, labels=vendors, autopct='%1.1f%%', startangle=140)
            ax.set_title("Vendor-wise Expense Distribution")
            fig.tight_layout()
            layout.addWidget(canvas)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load vendor expenses:\n{e}")

        widget.setLayout(layout)
        return widget
