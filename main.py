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
        f1 = self.polinom(self.inputs["x3_input"], self.inputs["f1k1_input"], self.inputs["f1k2_input"], self.inputs["f1k3_input"], self.inputs["f1k4_input"])
        f2 = self.polinom(self.inputs["x19_input"], self.inputs["f2k1_input"], self.inputs["f2k2_input"], self.inputs["f2k3_input"], self.inputs["f2k4_input"])
        f3 = self.polinom(self.inputs["x21_input"], self.inputs["f3k1_input"], self.inputs["f3k2_input"],self.inputs["f3k3_input"], self.inputs["f3k4_input"])
        f4 = self.polinom(self.inputs["x22_input"], self.inputs["f4k1_input"], self.inputs["f4k2_input"],self.inputs["f4k3_input"], self.inputs["f4k4_input"])
        f5 = self.polinom(self.inputs["x23_input"], self.inputs["f5k1_input"], self.inputs["f5k2_input"],self.inputs["f5k3_input"], self.inputs["f5k4_input"])
        f6 = self.polinom(self.inputs["x27_input"], self.inputs["f6k1_input"], self.inputs["f6k2_input"], self.inputs["f6k3_input"], self.inputs["f6k4_input"])
        f7 = self.polinom(self.inputs["x29_input"], self.inputs["f7k1_input"], self.inputs["f7k2_input"],self.inputs["f7k3_input"], self.inputs["f7k4_input"])
        f14 = self.polinom(self.inputs["x19_input"], self.inputs["f14k1_input"], self.inputs["f14k2_input"],self.inputs["f14k3_input"], self.inputs["f14k4_input"])
        f25 = self.polinom(self.inputs["x14_input"], self.inputs["f25k1_input"], self.inputs["f25k2_input"],self.inputs["f25k3_input"], self.inputs["f25k4_input"])
        f16 = self.polinom(self.inputs["x5_input"], self.inputs["f16k1_input"], self.inputs["f16k2_input"],self.inputs["f16k3_input"], self.inputs["f16k4_input"])
        f18 = self.polinom(self.inputs["x6_input"], self.inputs["f18k1_input"], self.inputs["f18k2_input"],self.inputs["f18k3_input"], self.inputs["f18k4_input"])
        f34 = self.polinom(self.inputs["x30_input"], self.inputs["f34k1_input"], self.inputs["f34k2_input"],self.inputs["f34k3_input"], self.inputs["f34k4_input"])

        f8 = self.polinom(self.inputs["x4_input"], self.inputs["f8k1_input"], self.inputs["f8k2_input"],
                          self.inputs["f8k3_input"], self.inputs["f8k4_input"])
        f9 = self.polinom(self.inputs["x20_input"], self.inputs["f9k1_input"], self.inputs["f9k2_input"],
                          self.inputs["f9k3_input"], self.inputs["f9k4_input"])
        f12 = self.polinom(self.inputs["x28_input"], self.inputs["f12k1_input"], self.inputs["f12k2_input"],
                           self.inputs["f12k3_input"], self.inputs["f12k4_input"])
        f10 = self.polinom(self.inputs["x22_input"], self.inputs["f10k1_input"], self.inputs["f10k2_input"],
                           self.inputs["f10k3_input"], self.inputs["f10k4_input"])
        f11 = self.polinom(self.inputs["x23_input"], self.inputs["f11k1_input"], self.inputs["f11k2_input"],
                           self.inputs["f11k3_input"], self.inputs["f11k4_input"])
        f13 = self.polinom(self.inputs["x29_input"], self.inputs["f13k1_input"], self.inputs["f13k2_input"],
                           self.inputs["f13k3_input"], self.inputs["f13k4_input"])
        f15 = self.polinom(self.inputs["x20_input"], self.inputs["f15k1_input"], self.inputs["f15k2_input"],
                           self.inputs["f15k3_input"], self.inputs["f15k4_input"])
        f21 = self.polinom(self.inputs["x12_input"], self.inputs["f21k1_input"], self.inputs["f21k2_input"],
                           self.inputs["f21k3_input"], self.inputs["f21k4_input"])
        f17 = self.polinom(self.inputs["x8_input"], self.inputs["f17k1_input"], self.inputs["f17k2_input"],
                           self.inputs["f17k3_input"], self.inputs["f17k4_input"])
        f19 = self.polinom(self.inputs["x10_input"], self.inputs["f19k1_input"], self.inputs["f19k2_input"],
                           self.inputs["f19k3_input"], self.inputs["f19k4_input"])
        f22 = self.polinom(self.inputs["x17_input"], self.inputs["f22k1_input"], self.inputs["f22k2_input"],
                           self.inputs["f22k3_input"], self.inputs["f22k4_input"])
        f20 = self.polinom(self.inputs["x11_input"], self.inputs["f20k1_input"], self.inputs["f20k2_input"],
                           self.inputs["f20k3_input"], self.inputs["f20k4_input"])
        f23 = self.polinom(self.inputs["x25_input"], self.inputs["f23k1_input"], self.inputs["f23k2_input"],
                           self.inputs["f23k3_input"], self.inputs["f23k4_input"])
        f24 = self.polinom(self.inputs["x30_input"], self.inputs["f24k1_input"], self.inputs["f24k2_input"],
                           self.inputs["f24k3_input"], self.inputs["f24k4_input"])

        f28 = self.polinom(self.inputs["x15_input"], self.inputs["f28k1_input"], self.inputs["f28k2_input"],
                           self.inputs["f28k3_input"], self.inputs["f28k4_input"])
        f29 = self.polinom(self.inputs["x16_input"], self.inputs["f29k1_input"], self.inputs["f29k2_input"],
                           self.inputs["f29k3_input"], self.inputs["f29k4_input"])
        f31 = self.polinom(self.inputs["x26_input"], self.inputs["f31k1_input"], self.inputs["f31k2_input"],
                           self.inputs["f31k3_input"], self.inputs["f31k4_input"])
        f33 = self.polinom(self.inputs["x26_input"], self.inputs["f33k1_input"], self.inputs["f33k2_input"],
                           self.inputs["f33k3_input"], self.inputs["f33k4_input"])
        f32 = self.polinom(self.inputs["x21_input"], self.inputs["f32k1_input"], self.inputs["f32k2_input"],
                           self.inputs["f32k3_input"], self.inputs["f32k4_input"])

        y2 = equation.dx2t(self.inputs["MPn_x2_input"],
                           f8,
                           f9,
                           f12,
                           self.inputs["MPk_x2_input"],
                           f10,
                           f11,
                           f13)

        y4 = equation.dx4t(self.inputs["MV_input"],
                           self.inputs["MZ_input"],
                           f15,
                           self.inputs["MC_input"])

        y6 = equation.dx6t(self.inputs["PT_input"],
                           f21,
                           self.inputs["PI_input"],
                           f17,
                           self.inputs["PJ_input"],
                           f19,
                           self.inputs["PD_input"],
                           f22,
                           self.inputs["PS_input"],
                           f20,
                           f23,
                           f24)

        y8 = equation.dx8t(self.inputs["An_input"],
                           self.inputs["Ak_input"],
                           self.inputs["P_input"])

        y10 = equation.dx10t(self.inputs["IDPn_input"],
                             self.inputs["IDPk_input"],
                             self.inputs["P_input"])

        y12 = equation.dx12t(self.inputs["BPn_x12_input"],
                             self.inputs["BPk_x12_input"],
                             self.inputs["P_input"])

        y14 = equation.dx14t(self.inputs["DS_input"],
                             f28,
                             self.inputs["DV_input"],
                             f29,
                             self.inputs["DP_input"])

        y16 = equation.dx16t(self.inputs["INn_input"],
                             self.inputs["INk_input"],
                             self.inputs["NPP_input"])

        y18 = equation.x18(self.inputs["AI_input"],
                           self.inputs["AIp_input"],
                           f31)

        y20 = equation.dx20t(self.inputs["PMn_input"],
                             self.inputs["PMk_input"],
                             self.inputs["PM_input"])

        y22 = equation.dx22t(self.inputs["OPn_input"],
                             self.inputs["OPk_input"])

        y24 = equation.dx24t(self.inputs["ISPn_input"],
                             self.inputs["ISPk_input"],
                             f33)

        y26 = equation.dx26t(self.inputs["IDPn_input"],
                             f32,
                             self.inputs["IDPk_input"])

        y28 = equation.dx28t(self.inputs["MRPn_input"],
                             self.inputs["MRPk_input"])

        y30 = equation.dx30t(self.inputs["RPn_input"],
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
        solution = solve_ivp(self.calculate, (0, 1), x)
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
