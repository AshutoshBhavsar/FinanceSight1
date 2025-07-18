# gui/gui_archive.py
from PyQt6.QtWidgets import QApplication
import os
import webbrowser
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt6.QtCore import Qt
from api_client import fetch_filtered_invoices

class ArchiveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📂 Invoice Archive")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        title = QLabel("📂 Archived Invoices")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Vendor", "Amount", "Date", "Category", "File"])
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 80)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 130)
        self.table.setColumnWidth(4, 320)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.cellClicked.connect(self.open_file)
        layout.addWidget(self.table)

        refresh_button = QPushButton("🔄 Refresh")
        refresh_button.setStyleSheet("background-color: #3498DB; color: white;")
        refresh_button.clicked.connect(self.load_data)
        layout.addWidget(refresh_button)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        try:
            invoices = fetch_filtered_invoices()
            self.table.setRowCount(len(invoices))

            for row_idx, invoice in enumerate(invoices):
                self.table.setItem(row_idx, 0, QTableWidgetItem(invoice["vendor"]))
                self.table.setItem(row_idx, 1, QTableWidgetItem(f"₹ {invoice['amount']:.2f}"))
                self.table.setItem(row_idx, 2, QTableWidgetItem(invoice["invoice_date"]))
                self.table.setItem(row_idx, 3, QTableWidgetItem(invoice["category"]))

                file_path = invoice.get("file_path")
                if file_path and os.path.exists(file_path):
                    item = QTableWidgetItem("🗂️ Open File")
                    item.setData(Qt.ItemDataRole.UserRole, file_path)
                else:
                    item = QTableWidgetItem("❌ Not Found")

                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                self.table.setItem(row_idx, 4, item)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load archived invoices:\n{e}")

    def open_file(self, row, column):
        if column == 4:
            item = self.table.item(row, column)
            file_path = item.data(Qt.ItemDataRole.UserRole)
            if file_path and os.path.exists(file_path):
                webbrowser.open(f"file:///{file_path}")
            else:
                QMessageBox.warning(self, "File Not Found", "The file path is missing or invalid.")
def show_archive():
    app = QApplication([])
    window = ArchiveWindow()
    window.show()
    app.exec()