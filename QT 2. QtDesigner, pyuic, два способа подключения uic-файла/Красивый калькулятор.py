import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('upload.ui', self)

        [i.clicked.connect(self.run) for i in self.buttonGroup_digits.buttons()]
        [i.clicked.connect(self.calc) for i in self.buttonGroup_binary.buttons()]
        self.btn_dot.clicked.connect(self.run)
        self.btn_eq.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        self.data = ''
        self.data_eval = ''

    def real_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)

    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            print(self.data_eval)
            self.result()

    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('')

    def run(self):
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)

    def sqrt(self):
        if self.data_eval:
            self.data_eval += '**0.5'
            self.result()

    def result(self):
        self.data = eval(self.data_eval)
        self.data_eval = str(self.data)
        self.table.display(self.data)
        self.data = ''

    def calc(self):
        if self.data_eval:
            self.result()
            if self.data_eval[-1] not in ['+', '-', '/', '*']:
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval) - 1] + self.sender().text()
            self.data_eval = self.data_eval.replace('^', '**')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())