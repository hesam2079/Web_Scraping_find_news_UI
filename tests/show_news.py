import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTextEdit, QScrollArea, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text File Viewer")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.label = QLabel()
        self.scroll_area.setWidget(self.label)

        self.load_file("result.txt")

    def load_file(self, filename):
        try:
            with open(filename, "r") as file:
                text = file.read()
                self.label.setText(text)
        except FileNotFoundError:
            self.label.setText("File not found")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
