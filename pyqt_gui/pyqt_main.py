from PyQt6.QtWidgets import QApplication
import sys
from pyqt_dashboard import DashboardWindow

app = QApplication(sys.argv)
window = DashboardWindow()
window.show()
sys.exit(app.exec())