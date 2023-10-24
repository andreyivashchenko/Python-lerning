import pytest
import allure
from DB.config import DB_SETTINGS
from DB.src.db import DB


@pytest.fixture(scope='session')
def db() -> DB:
    with allure.step('Подключаемся к БД'):
        _db = DB(DB_SETTINGS).connect_db().create_cursor()

    yield _db

    with allure.step('Закрываем курсор и соединение с БД'):
        _db.close_cursor().disconnect_db()
