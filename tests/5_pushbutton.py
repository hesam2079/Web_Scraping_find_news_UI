from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QDialog, QLabel, QPushButton, QMenu)
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

        self.label = QLabel('hi', self)
        self.label.move(0, 30)
        self.label.setFont(QFont('Arial', 20))

        image = QPixmap('CBFwNO.jpg')
        self.label.setPixmap(image)

        # movie = QMovie('mygif.gif')
        # self.movie = QLabel(self)
        # self.label.setMovie(movie)
        # movie.start()
        # movie.stop()

        self.button = QPushButton('QPushButton', self)
        self.button.setGeometry(0, 100, 100, 40)
        # self.button.setFont(QFont('Arial', 20))
        self.button.setIcon(QIcon('CBFwNO.jpg'))
        self.button.setIconSize(QSize(20, 30))

        menu = QMenu()
        menu.addAction('Copy')
        menu.addAction('Paste')
        menu.addAction('Cut')
        menu.setFont(QFont('Arial', 5, QFont.Weight.Bold))
        menu.setStyleSheet('background-color:red')
        self.button.setMenu(menu)

        self.button.clicked.connect(self.clicked)

    def clicked(self):
        # self.movie.stop()
        return 0


window = MyWindow()
window.show()
sys.exit(app.exec())
