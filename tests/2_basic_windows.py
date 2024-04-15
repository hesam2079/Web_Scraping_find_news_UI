from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys
from PyQt6.QtGui import QIcon

app = QApplication(sys.argv)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuBar().addMenu('File')
        self.statusBar().showMessage('Salam')
        self.setMaximumSize(500, 700)
        self.setMinimumSize(100, 100)
        self.setFixedSize(300, 400)
        self.setFixedWidth(300)
        self.setFixedHeight(400)
        self.setWindowTitle('Sport News grabber')
        self.setWindowOpacity(0.7)
        self.setWindowIcon(QIcon('CBFwNO.jpg'))

window = MyWindow()
window.show()
sys.exit(app.exec())
