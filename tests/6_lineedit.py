from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QDialog, QLabel, QPushButton, QMenu,
                             QLineEdit)
import sys
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuBar().addMenu('File')
        self.statusBar().showMessage('Salam')
        # self.setMaximumSize(500, 700)
        # self.setMinimumSize(100, 100)
        # self.setFixedSize(300, 400)
        self.setFixedWidth(300)
        self.setFixedHeight(400)
        self.setWindowTitle('Sport News grabber')
        self.setWindowOpacity(0.7)
        self.setWindowIcon(QIcon('CBFwNO.jpg'))

        self.label = QLabel('', self)
        self.label.move(0, 150)
        self.label.setFont(QFont('Arial', 20))
        self.label.setText('Hello :)')

        self.button = QPushButton('QPushButton', self)
        self.button.setGeometry(0, 100, 100, 40)
        # self.button.setFont(QFont('Arial', 20))
        # self.button.setIcon(QIcon('CBFwNO.jpg'))
        # self.button.setIconSize(QSize(20, 30))

        self.create_qline_edit()

        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText(self.qline_edit.text())
        if self.qline_edit.text() == 'clear':
            self.label.setText('')

    def create_qline_edit(self):
        self.qline_edit = QLineEdit(self)
        self.qline_edit.setGeometry(0, 50, 90, 30)
        self.qline_edit.setPlaceholderText('input text')

window = MyWindow()
window.show()
sys.exit(app.exec())
