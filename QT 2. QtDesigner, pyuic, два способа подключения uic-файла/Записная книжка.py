import sys
import io

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
   <widget class="QListWidget" name="contactList">
    <property name="geometry">
     <rect>
      <x>35</x>
      <y>281</y>
      <width>291</width>
      <height>191</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="contactName">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>190</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="contactNumber">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>230</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>190</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>230</y>
      <width>47</width>
      <height>13</height>
     </rect>
    </property>
    <property name="text">
     <string>Телефон</string>
    </property>
   </widget>
   <widget class="QPushButton" name="addContactBtn">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>210</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.addContactBtn.clicked.connect(self.write)

    def write(self):
        self.contactList.addItem(f'{self.contactName.text()} {self.contactNumber.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())