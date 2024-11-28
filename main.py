import sys
import json

from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel, QListWidget, \
    QPushButton, QLineEdit, QInputDialog, QMessageBox


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

        # Загрузка данных из json-файла
        try:
            with open('notes.json', 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

        # Привязка элементов к данным, кнопок к функциям
        self.lst_notes.addItems(self.data.keys())
        self.lst_notes.itemClicked.connect(self.show_note)
        self.btn_create_note.clicked.connect(self.create_note)
        self.btn_save_note.clicked.connect(self.save_note)
        self.btn_delete_note.clicked.connect(self.delete_note)
        self.btn_add_tag.clicked.connect(self.add_tag)
        self.btn_delete_tag.clicked.connect(self.delete_tag)
        self.btn_search_by_tag.clicked.connect(self.find_by_tag)

    # Вывод заметки
    def show_note(self):
        note_name = self.lst_notes.currentItem().text()
        n_text = self.data[note_name]["text"]
        n_tags = self.data[note_name]["tags"]

        self.text_note.setText(n_text)
        self.lst_tags.clear()
        self.lst_tags.addItems(n_tags)

    # создание заметки
    def create_note(self):
        note_name, result = QInputDialog.getText(window, "Добавить заметку", "Название заметки:")
        if result and not note_name in self.data.keys() and note_name != '':
            self.data[note_name] = {
                "text": "",
                "tags": []
            }
            self.lst_notes.addItem(note_name)

    # сохраняет все заметки в json-файл
    def save_all(self):
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    # сохраняет выбранную заметку
    def save_note(self):
        if self.lst_notes.currentItem():
            note_name = self.lst_notes.currentItem().text()
            self.data[note_name]['text'] = self.text_note.toPlainText()
            self.save_all()

    # удаление выбранной заметки
    def delete_note(self):
        if self.lst_notes.currentItem():
            note_name = self.lst_notes.currentItem().text()
            del self.data[note_name]

            cur_row = self.lst_notes.currentRow()
            self.lst_notes.takeItem(cur_row)

            self.lst_tags.clear()
            self.text_note.clear()

    # Добавление тега к заметке
    def add_tag(self):
        tag_name, result = QInputDialog.getText(window, "Добавить тег к заметке", "Название тега:")
        if self.lst_notes.currentItem() and result and len(tag_name) > 0:
            note_name = self.lst_notes.currentItem().text()
            self.data[note_name]['tags'].append(tag_name)
            self.lst_tags.addItem(tag_name)
            self.save_all()

    # Удаление тега
    def delete_tag(self):
        if self.lst_notes.currentItem() and self.lst_tags.currentItem():
            note_name = self.lst_notes.currentItem().text()
            tag_name = self.lst_tags.currentItem().text()
            self.data[note_name]['tags'].remove(tag_name)

            cur_row = self.lst_tags.currentRow()
            self.lst_tags.takeItem(cur_row)
            self.save_all()

    # поиск заметки по тегу
    def find_by_tag(self):
        if self.btn_search_by_tag.text() != 'Сбросить результаты поиска':
            if len(self.edit_tag.text()) > 0:
                text_to_find = self.edit_tag.text()
                result = {}
                for key, value in self.data.items():
                    if text_to_find in value['tags']:
                        result[key] = value

                self.lst_notes.clear()
                self.lst_tags.clear()
                self.text_note.clear()
                self.lst_notes.addItems(result.keys())

                self.btn_search_by_tag.setText('Сбросить результаты поиска')
            else:
                QMessageBox.warning(window, 'Предупреждение', 'Вы не ввели тег для поиска')
        else:
            self.lst_notes.clear()
            self.lst_tags.clear()
            self.text_note.clear()
            self.lst_notes.addItems(self.data.keys())
            self.btn_search_by_tag.setText('Искать заметки по тегу')


if __name__ == '__main__':
    # Запуск приложения
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
