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
    <height>619</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>70</y>
      <width>61</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя файла</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="filenameEdit">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>70</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>70</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Рассчитать</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>110</y>
      <width>131</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Максимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>121</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Минимальное значение</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>170</y>
      <width>101</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Среднее значение</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="maxEdit">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>110</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="minEdit">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>140</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="avgEdit">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>170</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>0,00</string>
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


def is_file_empty_or_whitespace_only(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Удаляем все пробельные символы и проверяем
            return content.strip() == ""
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return False


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.button.clicked.connect(self.run)

    def run(self):
        if len(self.filenameEdit.text()):
            try:
                with open(f'{self.filenameEdit.text()}', mode='r') as file:
                    if is_file_empty_or_whitespace_only(f'{self.filenameEdit.text()}'):
                        self.statusbar.showMessage("Указанный файл пуст")
                    else:
                        try:
                            data = []
                            for i in file:
                                data.append(int(i.strip()))
                            self.maxEdit.setText(f"{max(data)}")
                            self.minEdit.setText(f"{min(data)}")
                            self.avgEdit.setText("{:.2f}".format(sum(data) / len(data)))
                            self.statusbar.showMessage("")
                        except ValueError:
                            self.statusbar.showMessage("Файл содержит некорректные данные")
                            self.maxEdit.setText(f"0")
                            self.minEdit.setText(f"0")
                            self.avgEdit.setText(f"0.00")
            except FileNotFoundError:
                self.statusbar.showMessage("Указанный файл не существует")
                self.maxEdit.setText(f"0")
                self.minEdit.setText(f"0")
                self.avgEdit.setText(f"0.00")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())