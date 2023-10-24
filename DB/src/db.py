from psycopg2 import connect, OperationalError
from string import Template
from functools import wraps
import os


class SQL:
    """
        Класс для работы с .sql файлами
    """
    def __init__(self, path: str):
        self._scripts = {}

        for file in os.listdir(path):
            self._scripts[file] = Template(open(f'{path}/{file}').read())

    def get(self, name_file: str, **kwargs):
        return self._scripts.get(name_file, '').substitute(**kwargs)


def db_error_wrap(func):
    """
    Обертка для обработки ошибок при работе с БД
    :param func: функция, которую нужно "обернуть"
    :return: функция, "обернутая" обработкой ошибок
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError as err:
            print(f'Iternal database error: {err}')
            raise OperationalError

    return wrapper


class DB:
    def __init__(self, config: dict):
        self._connection = None
        self._db_config = config
        self._cursor = None
        self._sql = SQL(os.path.join(os.path.dirname(__file__), 'sql'))

    @db_error_wrap
    def connect_db(self):
        self._connection = connect(**self._db_config)
        self._connection.autocommit = True

        return self

    @db_error_wrap
    def disconnect_db(self):
        self._connection.close()

        return self

    @db_error_wrap
    def create_cursor(self):
        self._cursor = self._connection.cursor()

        return self

    @db_error_wrap
    def close_cursor(self):
        self._cursor.close()

        return self

    @db_error_wrap
    def get_user(self, id_user: int):
        sql = self._sql.get(name_file='get_user.sql', id=id_user)
        self._cursor.execute(sql)
        response = self._cursor.fetchone()

        return {self._cursor.description[i].name: response[i] for i in range(len(response))} \
            if response is not None else None

    def get_latest_record_in_users(self):
        sql = self._sql.get(name_file='get_latest_record.sql')
        self._cursor.execute(sql)
        response = self._cursor.fetchone()

        return response
