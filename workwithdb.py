# -*- coding: utf-8 -*-
import MySQLdb as MySQL  # pip install mysqlclient


class WorkWithDb:

    def __init__(self):
        pass

    def perform_connection(self):
        try_connection_count = 0
        print("Подключение к базе...")
        while try_connection_count <= 3:
            try:
                self.db = MySQL.connect(host="127.0.0.1", user="root", passwd="root", db="lazy24", charset="utf8mb4")
                print("Установлено соединение")
                try_connection_count = 0
                return True
            except Exception:
                try_connection_count += 1
                if try_connection_count <= 3:
                    print(f"Не удается подключиться к базе, выполняется попытка подключиться"
                          f" № {try_connection_count}...")
                else:
                    print("!!! Ошибка: Проблема с подключением к базе. Проверьте ваше интернет соединение")
                    return False

    def close_connection(self):
        self.db.close()

    def load_data(self, text_query):
        try_count = 0
        with self.db.cursor() as cur:
            try:
                # Запрос на получение данных
                cur.execute(text_query)
                # Извлечение данных
                self.data = cur.fetchall()

                print("Данные загружены")
            except Exception:
                print(f"Нет подключения к базе, выполняется попытка подключиться...")
                if self.perform_connection():
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
                print(f"Нет подключения к базе, выполняется попытка подключиться...")
                if self.perform_connection():
                    self.load_data(data)

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
                if self.perform_connection():
                    self.load_column_data(shipments_name)

    def get_data(self):
        return self.data

    def get_columns_names(self):
        return self.columns_names
