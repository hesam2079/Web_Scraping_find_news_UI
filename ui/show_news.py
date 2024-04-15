import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QVBoxLayout,
                             QMainWindow, QLineEdit, QPushButton)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer


def get_screen_size():
    # Get the geometry of the screen
    screen_geometry = QApplication.primaryScreen().geometry()
    # Calculate the size of the dialog
    dialog_size = screen_geometry.size() / 3  # One-third of the screen size
    return dialog_size


class ShowNewsWindow(QMainWindow):
    def __init__(self, app_name, creators, time_to_show=None):
        super().__init__()
        self.timer = None
        self.setWindowTitle(app_name)
        self.set_size()
        self.init_ui(creators)
        if time_to_show is not None:
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
        dialog_width = int(screen_width / 4)  # One-Second of the screen size
        dialog_height = int(screen_height / 4)  # One-Second of te screen size
        top_left_width = int((screen_width-dialog_width)/2)
        top_left_height = int((screen_height-dialog_height)/2)
        # Set the geometry with calculated values
        self.setGeometry(top_left_width, top_left_height, dialog_width, dialog_height)

    def init_ui(self, creators):
        layout = QVBoxLayout(self)

        describe_label = QLabel()
        describe_label.setText('')
        describe_label.setFont(QFont('Arial', 22))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowNewsWindow('Sport News Grabber', ['hesam'])
    window.show()
    sys.exit(app.exec())
