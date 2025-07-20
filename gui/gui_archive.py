from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QApplication
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor
from api_client import fetch_all_invoices
import webbrowser
import os

class ArchiveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📂 Invoice Archive")
        self.setFixedSize(900, 600)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        title = QLabel("📁 Archived Invoices")
        title.setStyleSheet("font-family: 'Segoe UI'; font-size: 18px; font-weight: bold; color: #2C3E50;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Vendor", "Amount", "Date", "Category", "File"])
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 80)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 130)
        self.table.setColumnWidth(4, 380)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setStyleSheet("""
            QTableWidget {
                font-family: 'Segoe UI';
                font-size: 13px;
                color: black;
                background-color: white;
            }
            QHeaderView::section {
                background-color: #D6EAF8;
                color: #2C3E50;
                font-weight: bold;
                padding: 5px;
                font-size: 13px;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.table.cellClicked.connect(self.open_file)
        layout.addWidget(self.table)

        refresh_button = QPushButton("🔄 Refresh")
        refresh_button.setStyleSheet("font-family: 'Segoe UI'; background-color: #3498DB; color: white; padding: 8px 16px; border: none; font-size: 13px;")
        refresh_button.clicked.connect(self.load_data)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        try:
            invoices = fetch_all_invoices()
            if not invoices:
                QMessageBox.information(self, "No Data", "No archived invoices found.")
                return

            self.table.setRowCount(len(invoices))

            for row_idx, invoice in enumerate(invoices):
                vendor = str(invoice.get("vendor", ""))
                amount = f"₹ {float(invoice.get('amount', 0)):.2f}"
                date = str(invoice.get("invoice_date", ""))
                category = str(invoice.get("category", ""))
                file_path = invoice.get("file_path")

                for col_idx, value in enumerate([vendor, amount, date, category]):
                    item = QTableWidgetItem(value)
                    item.setForeground(QBrush(QColor("#2C3E50")))
                    self.table.setItem(row_idx, col_idx, item)

                if file_path and os.path.exists(file_path):
                    file_item = QTableWidgetItem("🗂️ Open File")
                    file_item.setData(Qt.ItemDataRole.UserRole, file_path)
                elif file_path:
                    file_item = QTableWidgetItem("❌ Missing")
                    file_item.setData(Qt.ItemDataRole.UserRole, file_path)
                else:
                    file_item = QTableWidgetItem("❌ No Path")

                file_item.setForeground(QBrush(QColor("#2C3E50")))
                file_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.table.setItem(row_idx, 4, file_item)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load archive:\n{e}")

    def open_file(self, row, column):
        if column == 4:
            item = self.table.item(row, column)
            file_path = item.data(Qt.ItemDataRole.UserRole)
            if file_path and os.path.exists(file_path):
                webbrowser.open(f"file:///{file_path}")
            else:
                QMessageBox.warning(self, "File Not Found", "The file path is missing or invalid.")

# Optional standalone launcher
def show_archive():
    app = QApplication([])
    win = ArchiveWindow()
    win.show()
    app.exec()
