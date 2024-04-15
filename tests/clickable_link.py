import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

class ClickableLink(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        label = QLabel()
        label.setOpenExternalLinks(True)  # Allow the link to be opened in the default web browser
        label.setText('<a href="https://www.example.com">Click me!</a>')
        label.linkActivated.connect(self.openLink)  # Connect the linkActivated signal to the openLink method

        layout.addWidget(label)

    def openLink(self, url):
        QDesktopServices.openUrl(QUrl(url))  # Open the clicked link in the default web browser

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClickableLink()
    window.setWindowTitle('Clickable Link Example')
    window.show()
    sys.exit(app.exec())
