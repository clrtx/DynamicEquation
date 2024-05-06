import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QSpinBox
from form import Ui_Frame


class Form(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.inputs = {}
        self.relations = {}

        # show the login window
        self.show()
        self.ui.run_button.clicked.connect(self.run)

    def run(self):
        for input in self.findChildren(QLineEdit):
            name = input.objectName()
            if name != 'qt_spinbox_lineedit':
                self.inputs[input.objectName()] = self.parse(input)

        for relation in self.findChildren(QSpinBox):
            self.relations[relation.objectName()] = int(relation.text())


    def parse(self, input):
        try:
            return float(input.text())
        except:
            input.setPlaceholderText('Ошибка ввода')
            input.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_window = Form()
    sys.exit(app.exec())
