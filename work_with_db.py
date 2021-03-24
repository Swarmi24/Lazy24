# -*- coding: utf-8 -*-
import MySQLdb as MySQL  # pip install mysqlclient


class work_with_db():

    def __init__(self):
        pass

    def perform_connection(self):
        # надо прикрутить трай на случай ошибки подключения
        print("Подключение к базе...")
        try:
            self.db = MySQL.connect(host="127.0.0.1", user="root", passwd="root", db="lazy24", charset="utf8mb4")
            print("Установлено соединение")
        except Exception:
            print("Ошибка: не удалось подключится к базе")

    def close_connection(self):
        self.db.close()

    def load_data(self, text_query):
        with self.db.cursor() as cur:
            try:
                # Запрос на получение данных
                cur.execute(text_query)
                # Извлечение данных
                self.data = cur.fetchall()

                # Получаем названия столбцов таблицы
                cur.execute("""SHOW COLUMNS FROM shipments;""")
                columns_names = cur.fetchall()
                self.columns_names = [item[0] for item in columns_names]

                print("Данные загружены")
                cur.close()
            except Exception:
                print("Нет подключения к базе, выполняется попытка подключиться...")
                self.perform_connection()
                self.load_data(text_query)

    def insert_data(self, data):
        with self.db.cursor() as cur:
            try:
                # Запрос на занесение данных
                cur.execute(data)

                # Подтверждение
                self.db.commit()

                cur.close()
            except Exception:
                print("Нет подключения к базе, выполняется попытка подключиться...")
                self.perform_connection()
                self.insert_data(data)

    def load_column_data(self, shipments_name):
        with self.db.cursor() as cur:
            try:
                # Получаем названия столбцов таблицы
                cur.execute = cur.execute("""SHOW COLUMNS FROM {};""".format(shipments_name))
                columns_names = cur.fetchall()
                self.columns_names = [item[0] for item in columns_names]

                print("Название колонок загружено")
                cur.close()
            except Exception:
                print("Нет подключения к базе, выполняется попытка подключиться...")
                self.perform_connection()
                self.load_column_data(shipments_name)

    def get_data(self):
        return self.data

    def get_columns_names(self):
        return self.columns_names
