import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QVBoxLayout,
                             QDialog, QSpacerItem, QSizePolicy)
from PyQt6.QtGui import QDesktopServices, QFont
from PyQt6.QtCore import QUrl, Qt, QTimer


def get_screen_size():
    # Get the geometry of the screen
    screen_geometry = QApplication.primaryScreen().geometry()
    # Calculate the size of the dialog
    dialog_size = screen_geometry.size() / 3  # One-third of the screen size
    return dialog_size


class ClickableLink(QDialog):
    def __init__(self, app_name, creators, time_to_show):
        super().__init__()
        self.timer = None
        self.setWindowTitle(app_name)
        self.set_size()
        self.init_ui(creators)
        self.start_dialog_time(time_to_show)

    def start_dialog_time(self, time_to_show):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_dialog_time)
        self.timer.start(time_to_show)

    def close_dialog_time(self):
        self.timer.stop()
        self.close()

    def set_size(self):
        # Get the geometry of the screen
        screen_width = QApplication.primaryScreen().size().width()
        screen_height = QApplication.primaryScreen().size().height()
        # Calculate the size of the dialog
        dialog_width = int(screen_width / 2)  # One-Second of the screen size
        dialog_height = int(screen_height / 2)  # One-Second of te screen size
        top_left_width = int((screen_width-dialog_width)/2)
        top_left_height = int((screen_height-dialog_height)/2)
        # Set the geometry with calculated values
        self.setGeometry(top_left_width, top_left_height, dialog_width, dialog_height)

    def init_ui(self, creators):
        layout = QVBoxLayout(self)

        welcome_label = QLabel()
        welcome_label.setText("Welcome to Sport News Grabber")
        welcome_label.setFont(QFont('Arial', 50))

        creator1_label = QLabel()
        creator1_label.setOpenExternalLinks(True)  # Allow the link to be opened in the default web browser
        creator1_label.setText('<a href="https://hesam2079@gmail.com">Hesam2079</a>')
        creator1_label.linkActivated.connect(self.open_link)  # Connect the linkActivated signal to the openLink method
        creator2_label = QLabel()
        creator2_label.setOpenExternalLinks(True)  # Allow the link to be opened in the default web browser
        creator2_label.setText('<a href="https://hesam2079@gmail.com">Amirflh</a>')
        creator2_label.linkActivated.connect(self.open_link)  # Connect the linkActivated signal to the openLink method

        layout.addItem(QSpacerItem(20, 70))
        layout.addWidget(welcome_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        layout.addWidget(creator1_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(creator2_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(QSpacerItem(20, 40))

    @staticmethod
    def open_link(url):
        QDesktopServices.openUrl(QUrl(url))  # Open the clicked link in the default web browser


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClickableLink('Sport News Grabber', ['hesam'], 5000)
    window.show()
    sys.exit(app.exec())
