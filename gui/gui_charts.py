from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from api_client import fetch_monthly_trends
from PyQt6.QtWidgets import QApplication

class ChartsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 Monthly Expense Trends")
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()

        title = QLabel("📊 Monthly Expense Trends")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.canvas = FigureCanvas(Figure(figsize=(6, 4)))
        layout.addWidget(self.canvas)

        self.refresh_btn = QPushButton("🔄 Refresh")
        self.refresh_btn.setStyleSheet("background-color: #2ECC71; color: white;")
        self.refresh_btn.clicked.connect(self.plot_data)
        layout.addWidget(self.refresh_btn)

        self.setLayout(layout)
        self.plot_data()

    def plot_data(self):
        try:
            trends = fetch_monthly_trends()
            if not trends:
                raise ValueError("No data available")

            months = [t["month"] for t in trends]
            totals = [t["total"] for t in trends]

            ax = self.canvas.figure.clear()
            ax = self.canvas.figure.add_subplot(111)
            ax.plot(months, totals, marker="o", color="blue")
            ax.set_title("Monthly Expenses")
            ax.set_xlabel("Month")
            ax.set_ylabel("Total Amount (₹)")
            ax.grid(True)
            self.canvas.draw()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load chart:\n{e}")
def show_charts():
    app = QApplication([])
    window = ChartsWindow()
    window.show()
    app.exec()