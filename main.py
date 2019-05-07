from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_ok.clicked.connect(self.ok_clicked)
        self.ui.button_clear.clicked.connect(self.clear)
        self.ui.button_quit.clicked.connect(self.quit)

    def ok_clicked(self):
        sum_1 = (self.ui.spinBox_11.value() +
                 self.ui.spinBox_12.value() +
                 self.ui.spinBox_13.value() +
                 self.ui.spinBox_14.value())
        sum_2 = (self.ui.spinBox_21.value() +
                 self.ui.spinBox_22.value() +
                 self.ui.spinBox_23.value() +
                 self.ui.spinBox_24.value())
        sum_3 = (self.ui.spinBox_31.value() +
                 self.ui.spinBox_32.value() +
                 self.ui.spinBox_33.value() +
                 self.ui.spinBox_34.value())
        sum_4 = (self.ui.spinBox_41.value() +
                 self.ui.spinBox_42.value() +
                 self.ui.spinBox_43.value() +
                 self.ui.spinBox_44.value())
        sum_5 = (self.ui.spinBox_51.value() +
                 self.ui.spinBox_52.value() +
                 self.ui.spinBox_53.value() +
                 self.ui.spinBox_54.value())
        sum = sum_1 + sum_2 + sum_3 + sum_4 + sum_5
        self.ui.sum_1.setText(str(sum_1))
        self.ui.sum_2.setText(str(sum_2))
        self.ui.sum_3.setText(str(sum_3))
        self.ui.sum_4.setText(str(sum_4))
        self.ui.sum_5.setText(str(sum_5))
        self.ui.W_1.setText(str(sum_1 / sum))
        self.ui.W_2.setText(str(sum_2 / sum))
        self.ui.W_3.setText(str(sum_3 / sum))
        self.ui.W_4.setText(str(sum_4 / sum))
        self.ui.W_5.setText(str(sum_5 / sum))

    def clear(self):
        pass

    def quit(self):
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = MyWindow()
    mw.show()
    sys.exit(app.exec_())
