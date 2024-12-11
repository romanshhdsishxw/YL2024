import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLineEdit


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('AAAA')

        self.trick_button = QPushButton('->', self)
        self.trick_button.resize(self.trick_button.sizeHint())
        self.trick_button.move(100, 150)
        self.trick_button.clicked.connect(self.calc)

        self.first_value = QLineEdit(self)
        self.first_value.move(50, 90)

        self.second_value = QLineEdit(self)
        self.second_value.move(200, 90)

    def calc(self):
        self.second_value.setText(f'{eval(self.first_value.text())}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())