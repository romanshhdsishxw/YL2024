import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLineEdit, QPushButton, QPlainTextEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Order Form")

        self.prices = {
            "Чизбургер": 10,
            "Гамбургер": 20,
            "Кока-кола": 15,
            "Наггетсы": 30
        }

        self.checkboxes = []
        self.inputs = []

        self.layout = QVBoxLayout(self)

        self.create_order_inputs()

        self.orderButton = QPushButton("Заказать")
        self.orderButton.clicked.connect(self.place_order)

        self.order = QPlainTextEdit()
        self.order.setReadOnly(True)

        self.layout.addWidget(self.orderButton)
        self.layout.addWidget(self.order)

    def create_order_inputs(self):
        for dish in self.prices:
            checkbox = QCheckBox(dish)
            input_field = QLineEdit()
            input_field.setPlaceholderText("")
            input_field.setText("1")

            self.checkboxes.append(checkbox)
            self.inputs.append(input_field)

            self.layout.addWidget(checkbox)
            self.layout.addWidget(input_field)

    def place_order(self):
        self.order.clear()
        total_cost = 0
        order_details = []

        for checkbox, input_field, (dish, price) in zip(self.checkboxes, self.inputs, self.prices.items()):
            if checkbox.isChecked():
                try:
                    quantity = int(input_field.text())
                    if quantity < 1:
                        raise ValueError("Количество должно быть больше 0")
                    cost = quantity * price
                    total_cost += cost
                    order_details.append(f"{dish}-----{quantity}-----{cost}")
                except ValueError as e:
                    order_details.append(f"Ошибка ввода для {dish}: {str(e)}")

        self.order.appendPlainText('Ваш заказ\n')
        if order_details:
            self.order.appendPlainText("\n".join(order_details))

        self.order.appendPlainText(f"\nИтого: {total_cost}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())