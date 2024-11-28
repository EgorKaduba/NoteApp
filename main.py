import sys

from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel, QListWidget, \
    QPushButton, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Задаём базовые настройки окна (название, иконка, мин. размеры)
        self.setWindowTitle('NoteApp')
        self.setWindowIcon(QIcon('icon.ico'))
        self.setMinimumSize(600, 500)
        self.setStyleSheet("background-color: rgb(43, 41, 40);")
        font_id = QFontDatabase.addApplicationFont(fr'font.ttf')

        self.all_btn = list()

        if font_id == 0:
            font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
            self.font = QFont(font_name, 20)
        else:
            self.font = QFont()

        self.main_layout = QHBoxLayout()  # Главный layout (в нём распологаются все элементы)

        # Создание и заполнение левой колонки
        self.col_left = QVBoxLayout()
        self.text_note = QTextEdit()
        self.text_note.setStyleSheet("background-color: rgb(224, 218, 215);"
                                     "color: black;")
        self.text_note.setFont(self.font)
        self.col_left.addWidget(self.text_note)

        self.col_right = QVBoxLayout()  # Создание правой колонки

        # Создание блока со списком заметок
        self.layout1 = QVBoxLayout()
        self.lst_notes_label = QLabel('Список заметок:')
        self.lst_notes_label.setFont(self.font)
        self.lst_notes_label.setStyleSheet("color: rgb(224, 218, 215);")
        self.layout1.addWidget(self.lst_notes_label)

        self.lst_notes = QListWidget()
        self.lst_notes.setFont(self.font)
        self.lst_notes.setStyleSheet("color: black;"
                                     "background-color: rgb(224, 218, 215);")
        self.layout1.addWidget(self.lst_notes)

        # Блок для создания и удаления заметок (кнопки)
        self.layout2 = QHBoxLayout()

        self.btn_create_note = QPushButton('Создать заметку')
        self.btn_create_note.setFont(self.font)
        self.all_btn.append(self.btn_create_note)
        self.layout2.addWidget(self.btn_create_note)

        self.btn_delete_note = QPushButton('Удалить заметку')
        self.btn_delete_note.setFont(self.font)
        self.all_btn.append(self.btn_delete_note)
        self.layout2.addWidget(self.btn_delete_note)

        # Блоки для работы с тегами + кнопка сохранения заметки
        self.layout3 = QVBoxLayout()

        self.btn_save_note = QPushButton('Сохранить заметку')
        self.all_btn.append(self.btn_save_note)
        self.layout3.addWidget(self.btn_save_note)

        self.tags_label = QLabel('Список тегов:')
        self.tags_label.setFont(self.font)
        self.tags_label.setStyleSheet("color: rgb(224, 218, 215);")
        self.layout3.addWidget(self.tags_label)

        self.lst_tags = QListWidget()
        self.lst_tags.setFont(self.font)
        self.lst_tags.setStyleSheet("color: black;"
                                    "background-color: rgb(224, 218, 215);")
        self.layout3.addWidget(self.lst_tags)

        self.edit_tag = QLineEdit()
        self.edit_tag.setFont(self.font)
        self.edit_tag.setStyleSheet("color: black;"
                                    "background-color: rgb(224, 218, 215);"
                                    "border: 1px solid black;"
                                    "border-radius: 2px")
        self.edit_tag.setPlaceholderText('Введите тег...')
        self.layout3.addWidget(self.edit_tag)

        self.layout4 = QHBoxLayout()

        self.btn_add_tag = QPushButton('Добавить к заметке')
        self.all_btn.append(self.btn_add_tag)
        self.layout4.addWidget(self.btn_add_tag)

        self.btn_delete_tag = QPushButton('Открепить от заметки')
        self.all_btn.append(self.btn_delete_tag)
        self.layout4.addWidget(self.btn_delete_tag)

        self.layout5 = QHBoxLayout()
        self.btn_search_by_tag = QPushButton('Искать заметки по тегу')
        self.all_btn.append(self.btn_search_by_tag)
        self.layout5.addWidget(self.btn_search_by_tag)

        # Добавление стилей для всех кнопок
        for btn in self.all_btn:
            btn.setStyleSheet("background-color: rgb(224, 218, 215);"
                              "font-size: 15px;"
                              "border: 1px solid black;"
                              "border-radius: 5px;")

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
