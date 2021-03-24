'''Модель данных для таблицы, описываем модель, задаем ей значения и потом применяем
эту модель к таблице, для отображения данных. В данном случае, передаем в параметрах
стоковую модель данных, инициализируем её и переопределаем некоторые методы.'''
from PyQt5 import QtCore

class shipments_table_model(QtCore.QAbstractTableModel):
    '''Инициализация MyTableModel, передаем данные с базы и хэдер.
    Инициализируем абстрактную модель(наследование), записываем полученные данные в переменные класса
    MyTableModel'''

    def __init__(self, parent, data_list, column_list, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent)
        # column_list - названия столбцов в базе
        # Находим индексы столбцов date, volume, cost и comment - понадобятся в data_processing
        self.count_date = column_list.index('date')
        self.count_volume = column_list.index('volume')
        self.count_cost = column_list.index('cost')
        self.count_comm = column_list.index('comment')

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
                elif str_value == self.count_comm:
                    # Расчитываем и добавляем сумму
                    newrow.append(float(str_data_list[self.count_volume]) * float(str_data_list[self.count_cost]))
                    newrow.append(value)
                else:
                    newrow.append(value)
            # Добавляем строку в общий массив
            newdata.append(newrow)
            # Очищаем массив для строки
            newrow = []
        self.my_list = newdata