import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLineEdit


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('AAAA')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(100, 150)
        self.trick_button.clicked.connect(self.focus)

        self.first_value = QLineEdit(self)
        self.first_value.move(50, 90)

        self.second_value = QLineEdit(self)
        self.second_value.move(200, 90)

    def focus(self):
        if self.trick_button.text() == '->':
            self.second_value.setText(self.first_value.text())
            self.first_value.setText('')
            self.trick_button.setText('<-')
        else:
            self.first_value.setText(self.second_value.text())
            self.second_value.setText('')
            self.trick_button.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())