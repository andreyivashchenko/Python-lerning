from DB.src.schemas.user import User
import allure


from DB.src.base_classes.response import Response


@allure.feature('Тестирование PostgresDB "Booking website database"')
class TestDB:
    @allure.story('Тестирование получения данных о пользователе')
    def test_get_user(self, db):
        # response = db.get_user(id_user=0)
        # Response(response=response).validate(schema=User)
        res = db.get_latest_record_in_users()
        print(res)




