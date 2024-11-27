import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Задаём базовые настройки окна (название, иконка, мин. размеры)
        self.setWindowTitle('NoteApp')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setMinimumSize(600, 500)

        self.main_layout = QHBoxLayout()  # Главный layout (в нём распологаются все элементы)

        # Создание и заполнение левой колонки
        self.col_left = QVBoxLayout()
        self.text_note = QTextEdit()
        self.col_left.addWidget(self.text_note)

        self.col_right = QVBoxLayout()  # Создание правой колонки


if __name__ == '__main__':
    # Запуск приложения
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
