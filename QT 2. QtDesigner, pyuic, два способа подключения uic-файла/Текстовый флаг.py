import sys

from PyQt6.QtWidgets import QVBoxLayout, QApplication, QWidget, QPushButton, QLabel, QRadioButton, QButtonGroup


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Текстовый Флаг')
        self.setGeometry(300, 300, 400, 400)
        self.setFixedSize(300, 400)

        layout = QVBoxLayout()

        self.color_group_1 = QButtonGroup(self)
        self.color_group_2 = QButtonGroup(self)
        self.color_group_3 = QButtonGroup(self)

        self.button_color_blue_g1 = QRadioButton('Синий')
        self.button_color_red_g1 = QRadioButton('Красный')
        self.button_color_green_g1 = QRadioButton('Зелёный')

        self.color_group_1.addButton(self.button_color_blue_g1)
        self.color_group_1.addButton(self.button_color_red_g1)
        self.color_group_1.addButton(self.button_color_green_g1)

        layout.addWidget(self.button_color_blue_g1)
        layout.addWidget(self.button_color_red_g1)
        layout.addWidget(self.button_color_green_g1)

        self.button_color_blue_g2 = QRadioButton('Синий')
        self.button_color_red_g2 = QRadioButton('Красный')
        self.button_color_green_g2 = QRadioButton('Зелёный')

        self.color_group_2.addButton(self.button_color_blue_g2)
        self.color_group_2.addButton(self.button_color_red_g2)
        self.color_group_2.addButton(self.button_color_green_g2)

        layout.addWidget(self.button_color_blue_g2)
        layout.addWidget(self.button_color_red_g2)
        layout.addWidget(self.button_color_green_g2)

        self.button_color_blue_g3 = QRadioButton('Синий')
        self.button_color_red_g3 = QRadioButton('Красный')
        self.button_color_green_g3 = QRadioButton('Зелёный')

        self.color_group_3.addButton(self.button_color_blue_g3)
        self.color_group_3.addButton(self.button_color_red_g3)
        self.color_group_3.addButton(self.button_color_green_g3)

        layout.addWidget(self.button_color_blue_g3)
        layout.addWidget(self.button_color_red_g3)
        layout.addWidget(self.button_color_green_g3)

        self.result = QLabel('')
        self.make_flag = QPushButton('Сделать флаг')
        self.make_flag.clicked.connect(self.makeflag)

        layout.addWidget(self.result)
        layout.addWidget(self.make_flag)

        self.setLayout(layout)

    def selected_color(self, group):
        select_button = group.checkedButton()
        if select_button:
            return select_button.text()
        else:
            None

    def makeflag(self):
        color_1 = self.selected_color(self.color_group_1)
        color_2 = self.selected_color(self.color_group_2)
        color_3 = self.selected_color(self.color_group_3)

        if color_1 and color_2 and color_3:
            result_text = f'Цвета: {color_1}, {color_2} и {color_3}'
            self.result.setText(result_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())