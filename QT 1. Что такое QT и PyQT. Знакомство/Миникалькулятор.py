import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLCDNumber, QLineEdit


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('AAAA')

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.resize(self.calculate_button.sizeHint())
        self.calculate_button.move(0, 150)
        self.calculate_button.clicked.connect(self.calc)

        self.number_1 = QLineEdit(self)
        self.number_1.move(0, 50)

        self.number_2 = QLineEdit(self)
        self.number_2.move(150, 50)

        self.result_sum = QLCDNumber(self)
        self.result_sum.move(100, 100)

        self.result_sub = QLCDNumber(self)
        self.result_sub.move(100, 175)

        self.result_mul = QLCDNumber(self)
        self.result_mul.move(100, 250)

        self.result_div = QLCDNumber(self)
        self.result_div.move(100, 325)

    def calc(self):
        self.result_sum.display(f'{int(self.number_1.text()) + int(self.number_2.text())}')
        self.result_sub.display(f'{int(self.number_1.text()) - int(self.number_2.text())}')
        self.result_mul.display(f'{int(self.number_1.text()) * int(self.number_2.text())}')
        if self.number_2.text() == '0':
            self.result_div.display('Error')
        elif int(self.number_2.text()) > int(self.number_1.text()):
            self.result_div.display(f'{int(self.number_1.text()) / int(self.number_2.text())}'[:5])
        else:
            self.result_div.display(f'{round((int(self.number_1.text()) / int(self.number_2.text())), 3)}'[:5])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculator()
    ex.show()
    sys.exit(app.exec())
