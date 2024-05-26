import random
import sys
import base64
import io
import matplotlib.pyplot as plt
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QSpinBox

import equation
from form import Ui_Frame

from scipy.integrate import solve_ivp


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

        self.test()


    def calculate(self, t, arr):
        f1 = self.polinom(self, self.inputs["x3_input"], self.inputs["f1k1_input"], self.inputs["f1k2_input"], self.inputs["f1k3_input"], self.inputs["f1k4_input"])
        f2 = self.polinom(self, self.inputs["x19_input"], self.inputs["f2k1_input"], self.inputs["f2k2_input"], self.inputs["f2k3_input"], self.inputs["f2k4_input"])
        f3 = self.polinom(self, self.inputs["x21_input"], self.inputs["f3k1_input"], self.inputs["f3k2_input"],self.inputs["f3k3_input"], self.inputs["f3k4_input"])
        f4 = self.polinom(self, self.inputs["x22_input"], self.inputs["f4k1_input"], self.inputs["f4k2_input"],self.inputs["f4k3_input"], self.inputs["f4k4_input"])
        f5 = self.polinom(self, self.inputs["x23_input"], self.inputs["f5k1_input"], self.inputs["f5k2_input"],self.inputs["f5k3_input"], self.inputs["f5k4_input"])
        f6 = self.polinom(self, self.inputs["x27_input"], self.inputs["f6k1_input"], self.inputs["f6k2_input"], self.inputs["f6k3_input"], self.inputs["f6k4_input"])
        f7 = self.polinom(self, self.inputs["x29_input"], self.inputs["f7k1_input"], self.inputs["f7k2_input"],self.inputs["f7k3_input"], self.inputs["f7k4_input"])
        f14 = self.polinom(self, self.inputs["x19_input"], self.inputs["f14k1_input"], self.inputs["f14k2_input"],self.inputs["f14k3_input"], self.inputs["f14k4_input"])
        f25 = self.polinom(self, self.inputs["x14_input"], self.inputs["f25k1_input"], self.inputs["f25k2_input"],self.inputs["f25k3_input"], self.inputs["f25k4_input"])
        f16 = self.polinom(self, self.inputs["x5_input"], self.inputs["f16k1_input"], self.inputs["f16k2_input"],self.inputs["f16k3_input"], self.inputs["f16k4_input"])
        f18 = self.polinom(self, self.inputs["x6_input"], self.inputs["f18k1_input"], self.inputs["f18k2_input"],self.inputs["f18k3_input"], self.inputs["f18k4_input"])
        f34 = self.polinom(self, self.inputs["x30_input"], self.inputs["f34k1_input"], self.inputs["f34k2_input"],self.inputs["f34k3_input"], self.inputs["f34k4_input"])

        y2 = equation.dx2t(arr[1],
                           self.inputs["MPn_x2_input"],
                           self.relations["x2_x4_input"],
                           self.relations["x2_x20_input"],
                           self.relations["x2_x28_input"],
                           self.inputs["MPk_x2_input"],
                           self.relations["x2_x22_input"],
                           self.relations["x2_x23_input"],
                           self.relations["x2_x29_input"])

        y4 = equation.dx4t(arr[3],
                           self.inputs["MV_input"],
                           self.inputs["MZ_input"],
                           self.relations["x4_x20_input"],
                           self.inputs["MC_input"])

        y6 = equation.dx6t(arr[5],
                           self.inputs["PT_input"],
                           self.relations["x6_x12_input"],
                           self.inputs["PI_input"],
                           self.relations["x6_x8_input"],
                           self.inputs["PJ_input"],
                           self.relations["x6_x10_input"],
                           self.inputs["PD_input"],
                           self.relations["x6_x17_input"],
                           self.inputs["PS_input"])

        y8 = equation.dx8t(arr[7],
                           self.inputs["An_input"],
                           self.inputs["Ak_input"],
                           self.inputs["P_input"])

        y10 = equation.dx10t(arr[9],
                             self.inputs["IDPn_input"],
                             self.inputs["IDPk_input"],
                             self.inputs["P_input"])

        y12 = equation.dx12t(arr[11],
                             self.inputs["BPn_x12_input"],
                             self.inputs["BPk_x12_input"],
                             self.inputs["P_input"])

        y14 = equation.dx14t(arr[13],
                             self.inputs["DS_input"],
                             self.relations["x14_x15_input"],
                             self.inputs["DV_input"],
                             self.relations["x14_x16_input"],
                             self.inputs["DP_input"])

        y16 = equation.dx16t(arr[15],
                             self.inputs["INn_input"],
                             self.inputs["INk_input"],
                             self.inputs["NPP_input"])

        y18 = equation.x18(arr[17],
                           self.inputs["AI_input"],
                           self.inputs["AIp_input"],
                           self.relations["x18_x26_input"])

        y20 = equation.dx20t(arr[19],
                             self.inputs["PMn_input"],
                             self.inputs["PMk_input"],
                             self.inputs["PM_input"])

        y22 = equation.dx22t(arr[21],
                             self.inputs["OPn_input"],
                             self.inputs["OPk_input"])

        y24 = equation.dx24t(arr[23],
                             self.inputs["ISPn_input"],
                             self.inputs["ISPk_input"],
                             self.relations["x24_x26_input"])

        y26 = equation.dx26t(arr[25],
                             self.inputs["IDPn_input"],
                             self.relations["x26_x21_input"],
                             self.inputs["IDPk_input"])

        y28 = equation.dx28t(arr[27],
                             self.inputs["MRPn_input"],
                             self.inputs["MRPk_input"])

        y30 = equation.dx30t(arr[29],
                             self.inputs["RPn_input"],
                             self.inputs["RPk_input"],
                             self.inputs["P_input"])

        y1 = equation.dx1t(arr[0], self.inputs['BPn_x1_input'], self.inputs['BPk_x1_input'],
                           f1, f2, f6, f3, f4, f5, f7)
        y3 = equation.dx3t(arr[2], self.inputs['BV_input'], self.inputs['BZ_input'],
                           self.inputs['BC_input'], f14)

        y5 = equation.dx5t(arr[4], self.inputs['C_input'], self.inputs['P_input'])

        y7 = equation.dx7t(arr[6], self.inputs['G_input'], self.inputs['IG_input'],
                           self.inputs['NG_input'], self.inputs['F_input'], f25)

        y9 = equation.dx9t(arr[8], self.inputs['Vn_input'], self.inputs['Vk_input'],
                           self.inputs['P_input'], f16, f18)

        y11 = equation.dx11t(arr[10], self.inputs['DPn_input'], self.inputs['DPk_input'])

        y13 = equation.dx13t(arr[12], self.inputs['IB_input'], self.inputs['IN_input'],
                             self.inputs['IL_input'], self.inputs['F_input'])

        y15 = equation.dx15t(arr[14], self.inputs['JPn_x15_input'], self.inputs['JPk_x15_input'],
                             self.inputs['P_input'])

        y17 = equation.dx17t(arr[16], self.inputs['PPn_input'], self.inputs['PPk_input'],
                             self.inputs['P_input'])

        y19 = equation.dx19t(arr[18], self.inputs['PBn_input'], self.inputs['PBk_input'],
                             self.inputs['PB_input'])

        y21 = equation.dx21t(arr[20], self.inputs['IPn_input'], self.inputs['IPk_input'])

        y23 = equation.dx23t(arr[22], self.inputs['JPn_x23_input'], self.inputs['JPk_x23_input'])

        y25 = equation.dx25t(arr[24], self.inputs['JPn_x25_input'], self.inputs['JPk_x25_input'],
                             self.inputs['P_input'])

        y27 = equation.dx27t(arr[26], self.inputs['BRPn_input'], self.inputs['BRPk_input'])

        y29 = equation.dx29t(arr[28], self.inputs['SRPn_input'], self.inputs['SRPk_input'])

        y31 = equation.dx31t(arr[30], self.inputs['IR_input'], self.inputs['NR_input'],
                             self.inputs['F_input'], f34)

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
        return y

    def test(self):
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
        solution = solve_ivp(self.calculate, (0,1), x)
        plt.figure(figsize=(14, 9), dpi=100)
        # Plot the results
        for index, element in enumerate(solution.y):
            plt.plot(solution.t, solution.y[index], label=f'P{index}(t)')
        plt.xlabel('Время (мин)')
        # plt.close()
        plt.show()


        return solution
    def parse(self, input):
        try:
            return float(input.text())
        except:
            input.setPlaceholderText('Ошибка ввода')
            input.setText('0')

    def polinom(self, x, k1, k2, k3, k4):
        return (k1 * x ** 3) + (k2 * x ** 2) + (k3 * x) + k4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form_window = Form()
    sys.exit(app.exec())
