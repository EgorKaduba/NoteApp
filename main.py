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

        # Блок для работы с тегами + кнопка сохранения заметки
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


if __name__ == '__main__':
    # Запуск приложения
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
