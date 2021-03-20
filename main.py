# -*- coding: utf-8 -*-
# from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

import main_ui
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main_ui.MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
