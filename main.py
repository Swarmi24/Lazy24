# -*- coding: utf-8 -*-
# from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

import main_ui
import work_with_db
import sys

if __name__ == "__main__":
    db_work_obj = work_with_db.work_with_db()
    db_work_obj.perform_connection()
    db_work_obj.load_data()
    data = db_work_obj.get_select_result()
    header = ['№', 'Дата', 'База', '№ АБС', 'Клиент', 'Объем', 'Марка', 'Вид', 'Цена', 'Сумма']
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main_ui.MainWindow(data, header, db_work_obj)
    MainWindow.show()
    sys.exit(app.exec_())
