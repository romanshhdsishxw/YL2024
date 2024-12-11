import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 394, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.verticalLayoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.verticalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        # self.line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        # self.line.setObjectName("line")
        # self.verticalLayout.addWidget(self.line)
        self.addEventBtn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.addEventBtn.setObjectName("addEventBtn")
        self.verticalLayout.addWidget(self.addEventBtn)
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(410, 30, 256, 361))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addEventBtn.setText(_translate("MainWindow", "Добавить событие"))


class SimplePlanner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(669, 444)
        self.line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.addEventBtn.clicked.connect(self.add_task)

    def add_task(self):
        date = self.calendarWidget.selectedDate().toString('dd-MM-yyyy')
        txt = self.line.text()
        dt = self.timeEdit.time().toString()
        self.listWidget.addItem(f'{date} {dt} - {txt}')
        self.line.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
