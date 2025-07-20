from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from api_client import fetch_monthly_expense_trend, fetch_vendor_expense_distribution


class ChartsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Expense Charts")
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        title = QLabel("📈 Expense Analytics")
        title.setStyleSheet("font-family: 'Segoe UI'; font-size: 20px; font-weight: bold; color: #2C3E50; padding: 10px;")
        layout.addWidget(title)

        self.monthly_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.vendor_canvas = FigureCanvas(Figure(figsize=(5, 3)))

        chart_layout = QHBoxLayout()
        chart_layout.addWidget(self.monthly_canvas)
        chart_layout.addWidget(self.vendor_canvas)
        layout.addLayout(chart_layout)

        refresh_btn = QPushButton("🔄 Refresh Charts")
        refresh_btn.setStyleSheet("font-family: 'Segoe UI'; background-color: #2ECC71; color: white; font-weight: bold; font-size: 13px; padding: 10px;")
        refresh_btn.clicked.connect(self.plot_charts)
        layout.addWidget(refresh_btn)

        self.setLayout(layout)
        self.plot_charts()

    def plot_charts(self):
        try:
            # Monthly Trend Chart
            monthly_data = fetch_monthly_expense_trend()
            months = [item["month"] for item in monthly_data]
            totals = [item["total"] for item in monthly_data]

            self.monthly_canvas.figure.clear()
            ax1 = self.monthly_canvas.figure.add_subplot(111)
            ax1.plot(months, totals, marker='o', color='blue')
            ax1.set_title("Monthly Expense Trend", fontname='Segoe UI', fontsize=12)
            ax1.set_xlabel("Month", fontname='Segoe UI')
            ax1.set_ylabel("Total Amount", fontname='Segoe UI')
            ax1.grid(True)
            self.monthly_canvas.draw()

            # Vendor Distribution Chart
            vendor_data = fetch_vendor_expense_distribution()
            vendors = [item["vendor"] for item in vendor_data]
            totals = [item["total"] for item in vendor_data]

            self.vendor_canvas.figure.clear()
            ax2 = self.vendor_canvas.figure.add_subplot(111)
            ax2.bar(vendors, totals, color='orange')
            ax2.set_title("Vendor-wise Expenses", fontname='Segoe UI', fontsize=12)
            ax2.set_xlabel("Vendor", fontname='Segoe UI')
            ax2.set_ylabel("Total Amount", fontname='Segoe UI')
            ax2.tick_params(axis='x', rotation=45)
            ax2.grid(axis='y')
            self.vendor_canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Chart Error", f"Failed to load charts:\n{e}")
