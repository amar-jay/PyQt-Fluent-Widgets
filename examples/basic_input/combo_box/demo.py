# coding:utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCompleter, QHBoxLayout, QWidget
from qfluentwidgets import (
    ComboBox,
    EditableComboBox,
    FluentThemeColor,
    Theme,
    setFont,
    setTheme,
    setThemeColor,
)


class Demo(QWidget):
	def __init__(self):
		super().__init__()
		self.comboBox = ComboBox(self)
		self.hBoxLayout = QHBoxLayout(self)

		self.comboBox.setPlaceholderText("选择一个脑婆")

		items = ["shoko 🥰", "西宫硝子", "宝多六花", "小鸟游六花"]
		self.comboBox.addItems(items)
		self.comboBox.setCurrentIndex(-1)

		self.comboBox.currentTextChanged.connect(print)

		# self.comboBox.setPlaceholderText("选择一个脑婆")
		# self.comboBox.setCurrentIndex(-1)

		# NOTE: Completer is only applicable to EditableComboBox
		# self.completer = QCompleter(items, self)
		# self.comboBox.setCompleter(self.completer)

		self.resize(500, 500)
		self.hBoxLayout.addWidget(self.comboBox, 0, Qt.AlignCenter)
		self.setStyleSheet("Demo{background:white}")

		# setTheme(Theme.DARK)
		# setThemeColor(FluentThemeColor.DEFAULT_BLUE.color())
		# setFont(self.comboBox, 16)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = Demo()
	w.show()
	app.exec()
