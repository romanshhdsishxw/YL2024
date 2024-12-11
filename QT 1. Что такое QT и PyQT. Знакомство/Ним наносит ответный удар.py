import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class NimStrikesBack(QWidget):

    def check(self):
        self.output_count.setText(str(self.count))
        self.output_x.setText(str(self.X))
        if self.X == 0 and self.count > 0:
            self.result_label.setText('Поздравляем! Вы победили. Начинаем новую игру.')
            self.new_game()
        elif self.count == 0:
            self.result_label.setText('К сожалению, вы проиграли. Начнем заново.')
            self.new_game()

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 300, 720, 500)
        self.setWindowTitle('Ним наносит ответный удар')

        self.X = random.randint(1, 10)
        self.Y = random.randint(1, 10)
        self.Z = random.randint(-10, -1)
        self.count = 10

        self.result_label = QLabel(self)
        self.result_label.setText("                                                                                  ")
        self.result_label.setGeometry(0, 0, 720, 50)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btnp = QPushButton(f"+{self.Y}", self)
        self.btnp.setGeometry(30, 30, 100, 40)
        self.btnp.clicked.connect(self.plus)

        self.btnm = QPushButton(str(self.Z), self)
        self.btnm.setGeometry(150, 30, 100, 40)
        self.btnm.clicked.connect(self.minus)

        self.label_count = QLabel("Осталось ходов:", self)
        self.label_count.setGeometry(0, 80, 150, 30)

        self.output_count = QLineEdit(self)
        self.output_count.setGeometry(150, 80, 50, 30)
        self.output_count.setText(str(self.count))
        self.output_count.setReadOnly(True)

        self.label_x = QLabel("Текущее число:", self)
        self.label_x.setGeometry(0, 130, 150, 30)

        self.output_x = QLineEdit(self)
        self.output_x.setGeometry(150, 130, 50, 30)
        self.output_x.setText(str(self.x))
        self.output_x.setReadOnly(True)

    def plus(self):
        self.X += self.Y
        self.count -= 1
        self.check()

    def minus(self):
        self.X += self.Z
        self.count -= 1
        self.check()

    def new_game(self):
        self.X = random.randint(1, 10)
        self.Y = random.randint(1, 10)
        self.Z = random.randint(-10, -1)
        self.count = 10
        self.output_count.setText(str(self.count))
        self.output_x.setText(str(self.X))
        self.btnp.setText(f"+{self.Y}")
        self.btnm.setText(str(self.Z))
        self.result_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NimStrikesBack()
    window.show()
    sys.exit(app.exec())