import sys
import io
import random

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>160</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Получить</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="text_field">
    <property name="geometry">
     <rect>
      <x>193</x>
      <y>160</y>
      <width>251</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>23</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.button.clicked.connect(self.run)
        with open('files_txt/lines.txt', 'r') as file:
            self.txt = file.readlines()

    def run(self):
        self.text_field.setText(random.choice(self.txt).strip())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())