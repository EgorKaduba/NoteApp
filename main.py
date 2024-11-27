import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel, QListWidget, \
    QPushButton, QLineEdit


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

        # Создание блока со списком заметок
        self.layout1 = QVBoxLayout()
        self.lst_notes_label = QLabel('Список заметок:')
        self.layout1.addWidget(self.lst_notes_label)
        self.lst_notes = QListWidget()
        self.layout1.addWidget(self.lst_notes)

        # Блок для создания и удаления заметок (кнопки)
        self.layout2 = QHBoxLayout()
        self.btn_create_note = QPushButton('Создать заметку')
        self.layout2.addWidget(self.btn_create_note)
        self.btn_delete_note = QPushButton('Удалить заметку')
        self.layout2.addWidget(self.btn_delete_note)

        # Блоки для работы с тегами + кнопка сохранения заметки
        self.layout3 = QVBoxLayout()

        self.btn_save_note = QPushButton('Сохранить заметку')
        self.layout3.addWidget(self.btn_save_note)

        self.tags_label = QLabel('Список тегов:')
        self.layout3.addWidget(self.tags_label)

        self.lst_tags = QListWidget()
        self.layout3.addWidget(self.lst_tags)

        self.edit_tag = QLineEdit()
        self.edit_tag.setPlaceholderText('Введите тег...')
        self.layout3.addWidget(self.edit_tag)

        self.layout4 = QHBoxLayout()

        self.btn_add_tag = QPushButton('Добавить к заметке')
        self.layout4.addWidget(self.btn_add_tag)

        self.btn_delete_tag = QPushButton('Открепить от заметки')
        self.layout4.addWidget(self.btn_delete_tag)

        self.layout5 = QHBoxLayout()
        self.btn_search_by_tag = QPushButton('Искать заметки по тегу')
        self.layout5.addWidget(self.btn_search_by_tag)

        # Добавление layout-ов на экран
        self.col_right.addLayout(self.layout1)
        self.col_right.addLayout(self.layout2)
        self.col_right.addLayout(self.layout3)
        self.col_right.addLayout(self.layout4)
        self.col_right.addLayout(self.layout5)
        self.col_right.setSpacing(16)

        self.main_layout.addLayout(self.col_left)
        self.main_layout.addLayout(self.col_right)
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    # Запуск приложения
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
