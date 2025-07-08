from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog,
    QLineEdit, QComboBox, QMessageBox
)
from PyQt6.QtCore import Qt
import os

from ocr.extractor import extract_text_from_pdf, extract_text_from_docx
from parser import parse_invoice_data
from api_client import insert_invoice_api

class UploadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📤 Upload Financial Document")
        self.setFixedSize(500, 300)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        self.label_title = QLabel("Upload Financial Document")
        self.label_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_title)

        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("Choose PDF or DOCX file")
        self.file_path_input.setReadOnly(True)
        layout.addWidget(self.file_path_input)

        self.browse_btn = QPushButton("📁 Browse File")
        self.browse_btn.setStyleSheet("background-color: #3498DB; color: white;")
        self.browse_btn.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_btn)

        self.category_label = QLabel("Document Category:")
        layout.addWidget(self.category_label)

        self.category_cb = QComboBox()
        self.category_cb.addItems(["Invoice", "Profit & Loss Statement", "Expense Report"])
        layout.addWidget(self.category_cb)

        self.upload_btn = QPushButton("📥 Upload & Parse")
        self.upload_btn.setStyleSheet("background-color: #2ECC71; color: white;")
        self.upload_btn.clicked.connect(self.upload_and_parse)
        layout.addWidget(self.upload_btn)

        self.setLayout(layout)

    def browse_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Document", "", "Documents (*.pdf *.docx)")
        if file:
            self.file_path_input.setText(file)

    def upload_and_parse(self):
        path = self.file_path_input.text()
        category = self.category_cb.currentText()

        if not path:
            QMessageBox.warning(self, "No File", "Please select a file.")
            return

        try:
            ext = os.path.splitext(path)[1].lower()
            if ext == ".pdf":
                text = extract_text_from_pdf(path)
            elif ext == ".docx":
                text = extract_text_from_docx(path)
            else:
                raise ValueError("Unsupported file format")

            vendor, amount, date, _ = parse_invoice_data(text)

            if not vendor or not amount or not date:
                QMessageBox.warning(self, "Parse Error", "Missing Vendor, Amount or Date. Check document.")
                return

            success = insert_invoice_api(vendor, amount, date, category, path)
            if success:
                QMessageBox.information(self, "Success", f"✅ Uploaded:\n{vendor}, ₹{amount}, {date}")
                self.close()
            else:
                QMessageBox.critical(self, "Error", "❌ Failed to upload to backend.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to process file:\n{str(e)}")
