# -*- coding: utf-8 -*-
import MySQLdb as mysql  # pip install mysqlclient


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

    def load_data(self):
        with self.db.cursor() as cur:
            cur.execute("""select * from shipments""")  # Запрос на получение данных
            self.data = cur.fetchall()  # Получаем данные
            print("Данные загружены")
            # Пересоздание кортежа, с изменением формата даты (выглядит костылево, как минимум жестко задается
            # количество столбцов)
            self.data = [(mydata[0], mydata[1].strftime('%d.%m.%Y'), mydata[2], mydata[3], mydata[4], mydata[5],
                          mydata[6], mydata[7], mydata[8]) for mydata in self.data]
            print(str(self.data[1][1]))
            cur.close()

    def load_data_by_data(self, text_query):
        with self.db.cursor() as cur:
            cur.execute(text_query)  # Запрос на получение данных
            self.data = cur.fetchall()  # Получаем данные
            print("Данные загружены")
            # Пересоздание кортежа, с изменением формата даты (выглядит костылево, как минимум жестко задается
            # количество столбцов)
            print(self.data)
            if self.data:
                self.data = [(mydata[0], mydata[1].strftime('%d.%m.%Y'), mydata[2], mydata[3], mydata[4], mydata[5],
                              mydata[6], mydata[7], mydata[8]) for mydata in self.data]
            # print(str(self.data[1][1]))
            cur.close()
        # SELECT * FROM person WHERE name='Anna';

    # def insertnewdata(self):
    #     with self.db.cursor() as cur:
    #         cur.execute("""
    #         INSERT INTO shipments (date, base, abs_num, client_id, volume, brand, type, cost)
    #         VALUES ("2021-02-12","38","123","Кекер","5.2","400","5-20","6000")
    #         """)  # Запрос на занесение данных
    #         self.db.commit()
    #         print("Данные внесены")
    #         cur.close()

    def insert_data(self, data):
        with self.db.cursor() as cur:
            cur.execute(data)  # Запрос на занесение данных
            self.db.commit()
            print("Данные внесены 2")
            cur.close()

    def get_select_result(self):
        return self.data
