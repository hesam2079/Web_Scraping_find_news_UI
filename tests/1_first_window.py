from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys

app = QApplication(sys.argv)

windows = QWidget()

windows.show()

sys.exit(app.exec())