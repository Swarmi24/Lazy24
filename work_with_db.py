# -*- coding: utf-8 -*-
import MySQLdb as mysql  # pip install mysqlclient

import datetime

class work_with_db():

    def __init__(self):
        pass

    def perform_connection(self):
        # надо прикрутить трай на случай ошибки подключения
        print("Подключение к базе...")
        self.db = mysql.connect(host="127.0.0.1", user="root", passwd="root", db="lazy24", charset="utf8mb4")
        print("Установлено соединение")

    def close_connection(self):
        self.db.close()

    def load_data(self, text_query):
        with self.db.cursor() as cur:
            # Запрос на получение данных
            cur.execute(text_query)

            # Извлечение данных
            self.data = cur.fetchall()
            #row = [item for item in self.data]

            # Получаем названия столбцов таблицы
            cur.execute("""SHOW COLUMNS FROM shipments;""")
            columns_names = cur.fetchall()
            self.columns_names = [item[0] for item in columns_names]



            print("Данные загружены")
            # Пересоздание кортежа, с изменением формата даты (выглядит костылево, как минимум жестко задается количество столбцов)
            #self.data = [(mydata[0], mydata[1].strftime('%d.%m.%Y'), mydata[2], mydata[3], mydata[4], mydata[5],
            #              mydata[6], mydata[7], mydata[8]) for mydata in self.data]

            cur.close()


    def insert_data(self, data):
        with self.db.cursor() as cur:
            # Запрос на занесение данных
            cur.execute(data)

            # Подтверждение
            self.db.commit()

            print("Добавлена новая запись в БД")
            
            cur.close()

    def get_data(self):
        return self.data

    def get_columns_names(self):
        return self.columns_names
