# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

import main_ui
import sys

if __name__ == "__main__":
    # Создание объекта QApplication - руководит управляющей логикой ГПИ и основными настройками
    app = QtWidgets.QApplication(sys.argv)

    # Создание объекта основного окна приложения
    MainWindow = main_ui.MainWindow()
    MainWindow.show()

    sys.exit(app.exec_())
