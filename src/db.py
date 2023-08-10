import os
from psycopg2 import OperationalError, connect
from string import Template
from functools import wraps


class SQL:
    """
        Класс для работы с .sql файлами
    """

    def __init__(self, path: str):
        self._scripts = {}

        for file in os.listdir(path):
            self._scripts[file] = Template(open(f'{path}/{file}').read())

    def get(self, name: str, **kwargs):
        return self._scripts.get(name, '').substitute(**kwargs)


def db_error_wrap(func):
    """
    Обертка для обработки ошибок при работе с БД
    :param func: функция, которую нужно "обернуть"
    :return: функция, "обернутая" обработкой ошибок
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except OperationalError as error:
            print(f'Ошибка при работе с БД: {error}')

    return wrapper


class DB:
    """
    Класс для работы с базой данных
    """

    def __init__(self, settings: dict):
        self._connection = None
        self._settings = settings
        self._sql = SQL(os.path.join(os.path.dirname(__file__), 'sql'))

    @db_error_wrap
    def connect(self):
        """
        Создание подключения к базе данных на основе существующих настроек self.settings
        """
        self._connection = connect(**self._settings)
        self._connection.autocommit = True

    @db_error_wrap
    def create_user(self, data: dict):
        """
        Метод для добавления новой записи в таблицу users
        :param data: словарь с данными для добавления в таблицу users
        """
        sql = self._sql.get('create_user.sql', **data)
        cursor = self._connection.cursor()
        cursor.execute(sql)

    @db_error_wrap
    def get_info_user(self, id_user: int):
        """
        Метод для получения информации о пользователе
        :param id_user: id пользователя, о котором нужно получить информацию
        """
        sql = self._sql.get('get_info_user.sql', id=id_user)
        cursor = self._connection.cursor()
        cursor.execute(sql)

        return cursor.description

    @db_error_wrap
    def update_user(self, id_user: int, new_data: dict):
        """
        Метод для получения информации о пользователе
        :param id_user: id пользователя, о котором нужно получить информацию
        :param new_data: словарь с данными пользователя, которые нужно обновить
        """
        to_update = ','.join([f'{key}={new_data[key]}' if key != 'id' else None for key in new_data])
        sql = self._sql.get('update_user.sql', id=id_user, to_update=to_update)
        cursor = self._connection.cursor()
        cursor.execute(sql)

    @db_error_wrap
    def delete_user(self, id_user: int):
        """
        Метод для удаления пользователей
        :param id_user: id пользователя, которого нужно удалить
        """
        sql = self._sql.get('delete_user.sql', id=id_user)
        cursor = self._connection.cursor()
        cursor.execute(sql)
