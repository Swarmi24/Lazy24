# -*- coding: utf-8 -*-
import work_with_db

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QCompleter


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        # Объект для работы с базой
        self.db_work_obj = work_with_db.work_with_db()

        # Подключение к базе
        self.db_work_obj.perform_connection()



        #Названия столбцов (надо унести в базу)
        header = ['№', 'Дата', 'База', '№ АБС', 'Клиент', 'Объем', 'Марка', 'Вид', 'Цена', 'Сумма']

        # Настройки шрифта
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)

        # MainWindow
        QtWidgets.QMainWindow.__init__(self, *args)
        self.setWindowTitle("Lazy24 - Работа с базой")
        self.setObjectName("MainWindow")
        self.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget()

        # widget - верхняя строка: инфа о клиенте, сумма долга, сумма за день и тп
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 880, 30))
        self.widget.setAutoFillBackground(True)

        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 4, 861, 30))
        self.label_9.setFont(font)

        # widget_2 - меню в правой части: кнопки просмотр, отгрузка, изменить, оплата и тд
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(900, 10, 290, 680))
        self.widget_2.setAutoFillBackground(True)

        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.pushButton.clicked.connect(self.push_button_click)
        self.pushButton.setText("Просмотр")
        self.pushButton.setFont(font)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 10, 131, 41))
        self.pushButton_2.clicked.connect(self.push_button_2_click)
        self.pushButton_2.setText("Отгрузка")
        self.pushButton_2.setFont(font)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 131, 41))
        self.pushButton_3.clicked.connect(self.push_button_3_click)
        self.pushButton_3.setText("Изменить")
        self.pushButton_3.setFont(font)

        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 60, 131, 41))
        self.pushButton_4.setText("Оплата")
        self.pushButton_4.setFont(font)

        # widget_3 - форма для внесения отгрузок
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(900, 170, 291, 500))
        self.widget_3.setVisible(False)

        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.label_3.setFont(font)
        self.label_3.setText("№ Машины")

        self.edit_abs_num = QtWidgets.QLineEdit(self.widget_3)
        self.edit_abs_num.setGeometry(QtCore.QRect(10, 40, 101, 35))
        self.edit_abs_num.setFont(font)
        self.edit_abs_num.returnPressed.connect(self.edit_abs_num.focusNextChild)

        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 61, 31))
        self.label_2.setFont(font)
        self.label_2.setText("Марка")

        self.combo_type_1 = QtWidgets.QComboBox(self.widget_3)
        self.combo_type_1.setGeometry(QtCore.QRect(120, 40, 81, 35))
        self.combo_type_1.setFont(font)
        self.combo_type_1.setEditable(True)
        # Надо сделать подгрузку с базы
        list_combo_types_1 = ['', '75', '100', '150', '200', '250', '300', '350', '400']
        self.combo_type_1.addItems(list_combo_types_1)
        self.combo_type_1.completer().setCompletionMode(QCompleter.InlineCompletion)

        self.combo_type_2 = QtWidgets.QComboBox(self.widget_3)
        self.combo_type_2.setGeometry(QtCore.QRect(200, 40, 81, 35))
        self.combo_type_2.setFont(font)
        self.combo_type_2.setEditable(True)
        # Надо сделать подгрузку с базы
        list_combo_types_2 = ['', '5-20', 'р-р', 'пгс', '20-40', '50/50']
        self.combo_type_2.addItems(list_combo_types_2)
        self.combo_type_2.completer().setCompletionMode(QCompleter.InlineCompletion)

        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.label.setFont(font)
        self.label.setText("Объем")

        self.edit_volume = QtWidgets.QLineEdit(self.widget_3)
        self.edit_volume.setGeometry(QtCore.QRect(10, 110, 61, 35))
        self.edit_volume.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 51, 31))
        self.label_4.setFont(font)
        self.label_4.setText("Цена")

        self.edit_cost = QtWidgets.QLineEdit(self.widget_3)
        self.edit_cost.setGeometry(QtCore.QRect(80, 110, 101, 35))
        self.edit_cost.setFont(font)

        self.button_cost = QtWidgets.QPushButton(self.widget_3)
        self.button_cost.setGeometry(QtCore.QRect(185, 110, 41, 35))
        self.button_cost.setFont(font)
        self.button_cost.setText("...")

        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(230, 80, 41, 31))
        self.label_5.setFont(font)
        self.label_5.setText("База")

        self.combo_base = QtWidgets.QComboBox(self.widget_3)
        self.combo_base.setGeometry(QtCore.QRect(230, 110, 51, 35))
        self.combo_base.setFont(font)
        self.combo_base.setEditable(True)
        self.combo_base.setCurrentText("90")
        # Надо сделать подгрузку с базы
        list_combo_base = ['', '38р', '38б', '90']
        self.combo_base.addItems(list_combo_base)
        self.combo_base.completer().setCompletionMode(QCompleter.InlineCompletion)

        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 71, 31))
        self.label_6.setFont(font)
        self.label_6.setText("Дата")

        self.dateEdit = QtWidgets.QDateEdit(self.widget_3)
        self.dateEdit.setGeometry(QtCore.QRect(10, 180, 131, 35))
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 2, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setDateTime(datetime.now())

        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(150, 150, 111, 31))
        self.label_7.setFont(font)
        self.label_7.setText("Примечание")

        self.edit_comm = QtWidgets.QLineEdit(self.widget_3)
        self.edit_comm.setGeometry(QtCore.QRect(150, 180, 131, 35))
        self.edit_comm.setFont(font)
        self.edit_comm.setText("Блаблабла")

        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 71, 31))
        self.label_8.setFont(font)
        self.label_8.setText("Клиент")

        self.combo_client = QtWidgets.QComboBox(self.widget_3)
        self.combo_client.setGeometry(QtCore.QRect(10, 250, 151, 35))
        self.combo_client.setFont(font)
        self.combo_client.setEditable(True)
        # Надо сделать подгрузку с базы
        list_combo_client = ['', 'Элиста', 'Эверест', 'Ваятель', 'Руслан', 'Дима', 'ЖеняЦ']
        self.combo_client.addItems(list_combo_client)
        self.combo_client.completer().setCompletionMode(QCompleter.InlineCompletion)

        self.button_add = QtWidgets.QPushButton(self.widget_3)
        self.button_add.setGeometry(QtCore.QRect(170, 248, 111, 39))
        self.button_add.clicked.connect(self.button_add_click)
        self.button_add.setFont(font)
        self.button_add.setText("Добавить")
        self.button_add.setVisible(False)

        self.button_change = QtWidgets.QPushButton(self.widget_3)
        self.button_change.setGeometry(QtCore.QRect(170, 248, 111, 39))
        self.button_change.clicked.connect(self.button_change_click)
        self.button_change.setFont(font)
        self.button_change.setText("Изменить")
        self.button_change.setText
        self.button_change.setVisible(False)

        # widget_4 - форма для просмотра
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(900, 170, 291, 500))
        self.widget_4.setVisible(False)

        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget_4)
        self.dateEdit_2.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setDateTime(datetime.now())

        self.comboClient_2 = QtWidgets.QComboBox(self.widget_4)
        self.comboClient_2.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.comboClient_2.setFont(font)
        self.comboClient_2.setEditable(True)
        self.comboClient_2.addItems(list_combo_client)  # client widget_3
        self.comboClient_2.completer().setCompletionMode(QCompleter.InlineCompletion)

        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.label_10.setFont(font)
        self.label_10.setText("День")

        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 30, 101, 31))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("Просмотр")
        self.pushButton_5.clicked.connect(self.push_button_5_click)

        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 131, 31))
        self.label_11.setFont(font)
        self.label_11.setText("Клиент")

        self.pushButton_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 100, 101, 31))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("Просмотр")
        self.pushButton_6.clicked.connect(self.push_button_6_click)

        # Убрать виджет 5, при нажатии кнопки изменить - менять описание кнопки добавить и коннект на другой слот делать
        # При нажатии на кнопку добавить - менять обратно
        # Тк формы скорее всего будут всегда одинаковые, кроме кнопки

        # widget_5 - форма для внесения оплат
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(900, 170, 291, 500))
        self.widget_5.setVisible(False)

        # tableView
        # Первоначальная загрузка данных
        text_query = """select * from shipments"""
        self.db_work_obj.load_data(text_query)
        data = self.db_work_obj.get_data()
        columns_names = self.db_work_obj.get_columns_names()

        self.table_model = MyTableModel(self, data, columns_names, header)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setFont(font)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 880, 640))
        self.proxyModel = QtCore.QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.table_model)
        self.tableView.setModel(self.proxyModel)
        self.tableView.resizeColumnsToContents()
        self.tableView.setSortingEnabled(True)

        self.setCentralWidget(self.centralwidget)

    @pyqtSlot()  # декоратор, в 99% и без него будет работать, но вроде дает оптимизацию
    def push_button_click(self):
        self.widget_3.setVisible(False)
        self.widget_4.setVisible(True)

        text_query = """select * from shipments"""
        self.db_work_obj.load_data(text_query)

        data = self.db_work_obj.get_data()
        self.table_model.update_data(data)

    @pyqtSlot()  # декоратор, в 99% и без него будет работать, но вроде дает оптимизацию
    def push_button_2_click(self):
        self.widget_3.setVisible(True)
        self.widget_4.setVisible(False)

        self.button_add.setVisible(True)
        self.button_change.setVisible(False)

    @pyqtSlot()  # декоратор, в 99% и без него будет работать, но вроде дает оптимизацию
    # Действие кнопки меню "Изменить"
    # Отображение формы для изменения и подгрузка туда данных выбранной строки
    def push_button_3_click(self):
        self.widget_3.setVisible(True)
        self.widget_4.setVisible(False)

        self.button_add.setVisible(False)
        self.button_change.setVisible(True)

        my_index = self.tableView.selectedIndexes()[0]
        # Сохранение айди строки
        self.id_edit_row = int(self.tableView.model().index(my_index.row(), 0).data())

        # Копирование данных со строки в форму
        pars_my_date = self.tableView.model().index(my_index.row(), 1).data()
        self.dateEdit.setDate(QtCore.QDate(int(pars_my_date[6:10]), int(pars_my_date[3:5]), int(pars_my_date[0:2])))
        self.combo_base.setCurrentText(self.tableView.model().index(my_index.row(), 2).data())
        self.edit_abs_num.setText(self.tableView.model().index(my_index.row(), 3).data())
        self.combo_client.setCurrentText(self.tableView.model().index(my_index.row(), 4).data())
        self.edit_volume.setText(str(self.tableView.model().index(my_index.row(), 5).data()))
        self.combo_type_1.setCurrentText(self.tableView.model().index(my_index.row(), 6).data())
        self.combo_type_2.setCurrentText(self.tableView.model().index(my_index.row(), 7).data())
        self.edit_cost.setText(str(self.tableView.model().index(my_index.row(), 8).data()))

    @pyqtSlot()  # декоратор, в 99% и без него будет работать, но вроде дает оптимизацию
    def push_button_5_click(self):
        text_query = """select * from shipments WHERE date='{}'""".format(
            self.dateEdit_2.dateTime().toString("yyyy-MM-dd"))
        self.db_work_obj.load_data(text_query)
        data = self.db_work_obj.get_data()
        self.table_model.update_data(data)

    @pyqtSlot()  # декоратор, в 99% и без него будет работать, но вроде дает оптимизацию
    def push_button_6_click(self):
        print(self.comboClient_2.currentText())
        text_query = """select * from shipments WHERE client_id='{}'""".format(self.comboClient_2.currentText())
        self.db_work_obj.load_data(text_query)
        data = self.db_work_obj.get_data()
        summa = 0.0
        for mydata in data:
            summa = summa + (float(mydata[5]) * float(mydata[8]))
        self.label_9.setText("{} | Долг: {}".format(str(self.comboClient_2.currentText()), str(summa)))
        self.table_model.update_data(data)

    @pyqtSlot()
    def button_add_click(self):
        # Формирование SQL запроса для добавления отгрузки
        new_add_data = '''
		INSERT INTO shipments (date, base, abs_num, client_id, volume, brand, type, cost)
        VALUES ("{}","{}","{}","{}","{}","{}","{}","{}")
		'''.format(self.dateEdit.dateTime().toString("yyyy-MM-dd"), self.combo_base.currentText(),
                   self.edit_abs_num.text(),
                   self.combo_client.currentText(), self.edit_volume.text(), self.combo_type_1.currentText(),
                   self.combo_type_2.currentText(),
                   self.edit_cost.text())

        # Исполнение запроса через объект для работы с базой
        self.db_work_obj.insert_data(new_add_data)
        print("Добавлена новая запись в БД")

    @pyqtSlot()
    def button_change_click(self):
        # Формирование SQL запроса для изменения отгрузки
        new_change_data = '''
		UPDATE shipments 
        SET date = '{}', base = '{}', abs_num = '{}', client_id = '{}', volume = '{}', brand = '{}', type = '{}', cost = '{}'
        WHERE id_shipment = '{}'
		'''.format(self.dateEdit.dateTime().toString("yyyy-MM-dd"), self.combo_base.currentText(),
                   self.edit_abs_num.text(),
                   self.combo_client.currentText(), self.edit_volume.text(),
                   self.combo_type_1.currentText(), self.combo_type_2.currentText(),
                   self.edit_cost.text(), self.id_edit_row)
        print(new_change_data)
        # Исполнение запроса через объект для работы с базой     
        self.db_work_obj.insert_data(new_change_data)
        print("Внесены изменения в запись в базе")

    def closeEvent(self, event):
        print("Уходим, уходим...")
        self.db_work_obj.close_connection()
        super(MainWindow, self).closeEvent(event)


'''Модель данных для таблицы, описываем модель, задаем ей значения и потом применяем
эту модель к таблице, для отображения данных. В данном случае, передаем в параметрах
стоковую модель данных, инициализируем её и переопределаем некоторые методы.'''


class MyTableModel(QtCore.QAbstractTableModel):
    '''Инициализация MyTableModel, передаем данные с базы и хэдер.
    Инициализируем абстрактную модель(наследование), записываем полученные данные в переменные класса
    MyTableModel'''

    def __init__(self, parent, data_list, column_list, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent)
        # column_list - названия столбцов в базе
        # Находим индексы столбцов date, volume и cost - понадобятся в data_processing
        self.count_date = column_list.index('date')
        self.count_volume = column_list.index('volume')
        self.count_cost = column_list.index('cost')
        
        # Обработка данных   
        self.data_processing(data_list)
        
        self.header = header

    def rowCount(self, *args, **kwargs):
        return len(self.my_list)

    def columnCount(self, *args, **kwargs):
        return len(self.my_list[0])

    def data(self, index, role):
        if not index.isValid() or role != QtCore.Qt.DisplayRole:
            return None
        return self.my_list[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def update_data(self, data_list):
        self.beginResetModel()
        if data_list:
            self.data_processing(data_list)
        else:
            self.my_list = [["0" for i in range(len(self.header))]]
        self.endResetModel()

    # Обработка данных полученных с базы:
    # 1 - меняем формат даты с гггг-мм-дд на дд.мм.гггг
    # 2 - добавляем столбец суммы (стоимость * объем)
    # Данные с базы приходят в виде кортежа и его нельзя менять, поэтому создается новый массив
    def data_processing(self, data_list):
        # Для обработанной строки
        newrow = []
        # Для массива обработанных строк
        newdata = []
        # Перебираем строки (str_data_list) и элементы (str_value) в строках
        # count_date, count_volume, count_cost - вычисляются при инициализация модели
        for str_data_list in data_list:
            for str_value, value in enumerate(str_data_list):
                if (str_value == self.count_date):
                    # Изменение формата даты
                    newrow.append(value.strftime('%d.%m.%Y'))
                else:
                    newrow.append(value)
            # Расчитываем и добавляем сумму
            newrow.append( float(str_data_list[self.count_volume]) * float(str_data_list[self.count_cost]) )
            # Добавляем строку в общий массив
            newdata.append(newrow)
            # Очищаем массив для строки
            newrow=[]
        self.my_list = newdata