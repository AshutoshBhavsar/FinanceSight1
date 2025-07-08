from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from pyqt_upload import UploadWindow
from pyqt_invoices import InvoicesWindow

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📊 FinanceSight Dashboard")
        self.setFixedSize(400, 500)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("FinanceSight Dashboard"))

        upload_btn = QPushButton("Upload Invoice")
        upload_btn.clicked.connect(self.open_upload)
        layout.addWidget(upload_btn)

        invoices_btn = QPushButton("View Invoices")
        invoices_btn.clicked.connect(self.open_invoices)
        layout.addWidget(invoices_btn)

        self.setLayout(layout)

    def open_upload(self):
        self.upload_window = UploadWindow()
        self.upload_window.show()

    def open_invoices(self):
        self.invoice_window = InvoicesWindow()
        self.invoice_window.show()