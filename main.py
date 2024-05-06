import random
import sys

import matplotlib.pyplot
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QSpinBox

import equation
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

        for input in self.findChildren(QLineEdit):
            name = input.objectName()
            if name != 'qt_spinbox_lineedit':
                input.setText(str(random.randint(1, 10)))

    def run(self):

        try:
            for input in self.findChildren(QLineEdit):
                name = input.objectName()
                if name != 'qt_spinbox_lineedit':
                    self.inputs[input.objectName()] = self.parse(input)

            for relation in self.findChildren(QSpinBox):
                self.relations[relation.objectName()] = int(relation.text())
        except:
            return

        y2 = equation.dx2t(self.inputs["x2_input"],
                           self.inputs["MPn_x2_input"],
                           self.relations["x2_x4_input"],
                           self.relations["x2_x20_input"],
                           self.relations["x2_x28_input"],
                           self.inputs["MPk_x2_input"],
                           self.relations["x2_x22_input"],
                           self.relations["x2_x23_input"],
                           self.relations["x2_x29_input"])

        y4 = equation.dx4t(self.inputs["x4_input"],
                           self.inputs["MV_input"],
                           self.inputs["MZ_input"],
                           self.relations["x4_x20_input"],
                           self.inputs["MC_input"])

        y6 = equation.dx6t(self.inputs["x6_input"],
                           self.inputs["PT_input"],
                           self.relations["x6_x12_input"],
                           self.inputs["PI_input"],
                           self.relations["x6_x8_input"],
                           self.inputs["PJ_input"],
                           self.relations["x6_x10_input"],
                           self.inputs["PD_input"],
                           self.relations["x6_x17_input"],
                           self.inputs["PS_input"])

        y8 = equation.dx8t(self.inputs["x8_input"],
                           self.inputs["An_input"],
                           self.inputs["Ak_input"],
                           self.inputs["P_input"])

        y10 = equation.dx10t(self.inputs["x10_input"],
                             self.inputs["IDPn_input"],
                             self.inputs["IDPk_input"],
                             self.inputs["P_input"])

        y12 = equation.dx12t(self.inputs["x12_input"],
                             self.inputs["BPn_x12_input"],
                             self.inputs["BPk_x12_input"],
                             self.inputs["P_input"])

        y14 = equation.dx14t(self.inputs["x14_input"],
                             self.inputs["DS_input"],
                             self.inputs["x14_x15_input"],
                             self.inputs["DV_input"],
                             self.inputs["x14_x16_input"],
                             self.inputs["DP_input"])

        y16 = equation.dx16t(self.inputs["x16_input"],
                             self.inputs["INn_input"],
                             self.inputs["INk_input"],
                             self.inputs["NPP_input"])

        y18 = equation.x18(self.inputs["x18_input"],
                           self.inputs["AI_input"],
                           self.inputs["AIp_input"],
                           self.relations["x18_x26_input"])

        y20 = equation.dx20t(self.inputs["x20_input"],
                             self.inputs["PMn_input"],
                             self.inputs["PMk_input"],
                             self.inputs["PM_input"])

        y22 = equation.dx22t(self.inputs["x22_input"],
                             self.inputs["OPn_input"],
                             self.inputs["OPk_input"])

        y24 = equation.dx24t(self.inputs["x24_input"],
                             self.inputs["ISPn_input"],
                             self.inputs["ISPk_input"],
                             self.relations["x24_x26_input"])

        y26 = equation.dx26t(self.inputs["x26_input"],
                             self.inputs["IDPn_input"],
                             self.relations["x26_x21_input"],
                             self.inputs["IDPk_input"])

        y28 = equation.dx28t(self.inputs["x28_input"],
                             self.inputs["MRPn_input"],
                             self.inputs["MRPk_input"])

        y30 = equation.dx30t(self.inputs["x30_input"],
                             self.inputs["RPn_input"],
                             self.inputs["RPk_input"],
                             self.inputs["P_input"])

        y1 = equation.dx1t(self.inputs['x1_input'], self.inputs['BPn_x1_input'], self.inputs['BPk_x1_input'],
                           self.inputs['x1_x3_input'], self.inputs['x1_x19_input'], self.inputs['x1_x27_input'],
                           self.inputs['x1_x21_input'], self.inputs['x1_x22_input'], self.inputs['x1_x23_input'],
                           self.inputs['x1_x29_input'])
        y3 = equation.dx3t(self.inputs['x3_input'], self.inputs['BV_input'], self.inputs['BZ_input'],
                           self.inputs['BC_input'], self.inputs['x3_x19_input'])

        y5 = equation.dx5t(self.inputs['x5_input'], self.inputs['C_input'], self.inputs['P_input'])

        y7 = equation.dx7t(self.inputs['x7_input'], self.inputs['G_input'], self.inputs['IG_input'],
                           self.inputs['NG_input'], self.inputs['F_input'], self.inputs['x7_x14_input'])

        y9 = equation.dx9t(self.inputs['x9_input'], self.inputs['Vn_input'], self.inputs['Vk_input'],
                           self.inputs['P_input'], self.inputs['x9_x5_input'], self.inputs['x9_x6_input'])

        y11 = equation.dx11t(self.inputs['x11_input'], self.inputs['DBn_input'], self.inputs['DBk_input'])

        y13 = equation.dx13t(self.inputs['x13_input'], self.inputs['IB_input'], self.inputs['IN_input'],
                             self.inputs['IL_input'], self.inputs['F_input'])

        y15 = equation.dx15t(self.inputs['x15_input'], self.inputs['JPn_x15_input'], self.inputs['JPk_x15_input'],
                             self.inputs['P_input'])

        y17 = equation.dx17t(self.inputs['x17_input'], self.inputs['PPn_input'], self.inputs['PPk_input'],
                             self.inputs['P_input'])

        y19 = equation.dx19t(self.inputs['x19_input'], self.inputs['PBn_input'], self.inputs['PBk_input'],
                             self.inputs['PB_input'])

        y21 = equation.dx21t(self.inputs['x21_input'], self.inputs['IPn_input'], self.inputs['IPk_input'])

        y23 = equation.dx23t(self.inputs['x23_input'], self.inputs['JPn_x23_input'], self.inputs['JPk_x23_input'])

        y25 = equation.dx25t(self.inputs['x25_input'], self.inputs['JPn_x25_input'], self.inputs['JPk_x25_input'],
                             self.inputs['P_input'])

        y27 = equation.dx27t(self.inputs['x27_input'], self.inputs['BRPn_input'], self.inputs['BRPk_input'])

        y29 = equation.dx29t(self.inputs['x29_input'], self.inputs['SRPn_input'], self.inputs['SRPk_input'])

        y31 = equation.dx31t(self.inputs['x31_input'], self.inputs['IR_input'], self.inputs['NR_input'],
                             self.inputs['F_input'], self.inputs['x31_x30_input'])

        x = [self.inputs["x1_input"],
             self.inputs["x2_input"],
             self.inputs["x3_input"],
             self.inputs["x4_input"],
             self.inputs["x5_input"],
             self.inputs["x6_input"],
             self.inputs["x7_input"],
             self.inputs["x8_input"],
             self.inputs["x9_input"],
             self.inputs["x10_input"],
             self.inputs["x11_input"],
             self.inputs["x12_input"],
             self.inputs["x13_input"],
             self.inputs["x14_input"],
             self.inputs["x15_input"],
             self.inputs["x16_input"],
             self.inputs["x17_input"],
             self.inputs["x18_input"],
             self.inputs["x19_input"],
             self.inputs["x20_input"],
             self.inputs["x21_input"],
             self.inputs["x22_input"],
             self.inputs["x23_input"],
             self.inputs["x24_input"],
             self.inputs["x25_input"],
             self.inputs["x26_input"],
             self.inputs["x27_input"],
             self.inputs["x28_input"],
             self.inputs["x29_input"],
             self.inputs["x30_input"],
             self.inputs["x31_input"]]
        y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23,
             y24, y25, y26, y27, y28, y29, y30, y31]
        matplotlib.pyplot.plot(x, y)
        matplotlib.pyplot.show()

    def parse(self, input):
        try:
            return float(input.text())
        except:
            input.setPlaceholderText('Ошибка ввода')
            input.setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_window = Form()
    sys.exit(app.exec())
