import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NoteApp')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setMinimumSize(600, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
