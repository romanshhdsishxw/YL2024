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
   <widget class="QDoubleSpinBox" name="alert_value">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>10</y>
      <width>381</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="text1">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>50</y>
      <width>221</width>
      <height>221</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="text2">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>50</y>
      <width>221</width>
      <height>221</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="checkBtn">
    <property name="geometry">
     <rect>
      <x>141</x>
      <y>280</y>
      <width>311</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Сравнить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>13</y>
      <width>101</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Порог срабатывания (%)</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>40</y>
      <width>35</width>
      <height>10</height>
     </rect>
    </property>
    <property name="text">
     <string>Текст 1</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>40</y>
      <width>35</width>
      <height>10</height>
     </rect>
    </property>
    <property name="text">
     <string>Текст 2</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>18</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.checkBtn.clicked.connect(self.test)

    def test(self):
        set1 = set([s for s in self.text1.toPlainText().strip().split('\n')])
        set2 = set([s for s in self.text2.toPlainText().strip().split('\n')])
        proc = len(set1 & set2) / len(set1 | set2) * 100
        t = '{:.' + str(2) + 'f}'
        if proc >= self.alert_value.value():
            self.statusBar().showMessage(f'Тексты похожи на {t.format(proc)}%, плагиат')
        else:
            self.statusBar().showMessage(f'Тексты похожи на {t.format(proc)}%, не плагиат')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())