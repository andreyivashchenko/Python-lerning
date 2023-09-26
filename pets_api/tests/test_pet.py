import pytest
import requests

from pets_api.src.baseclasses.response import Response
from pets_api.src.schemas.pet import Pet
from pets_api.src.generators.pet import PetGenerator
from pets_api.configuration import BASE_URL


class TestPetsApi:
    @pytest.mark.create
    def test_post_new_pet_correct(self):
        response = requests.post(url=BASE_URL, json=PetGenerator().build())

        Response(response=response).assert_status_code(200).validate(Pet)

        id_to_delete = f'{response.json()["id"]}'
        requests.delete(url=BASE_URL + id_to_delete)

    @pytest.mark.create
    def test_post_new_pet_incorrect(self):
        response = requests.post(url=BASE_URL)

        Response(response=response).assert_status_code(415)

    @pytest.mark.parametrize('adding_a_pet_by_id', ['with delete'], indirect=True)
    @pytest.mark.create
    def test_post_existing_pet_correct(self, adding_a_pet_by_id):
        params = {'name': 'Vasya', 'status': 'sold'}
        id_pet = adding_a_pet_by_id
        response = requests.post(url=BASE_URL + f'/{id_pet}', params=params)

        Response(response=response).assert_status_code(200).assert_message(id_pet)

    @pytest.mark.skip("Нет проверки данных")
    @pytest.mark.parametrize('adding_a_pet_by_id', ['with delete'], indirect=True)
    @pytest.mark.create
    def test_post_existing_pet_incorrect(self, adding_a_pet_by_id):
        params = {'name': 'Барсик', 'status': 'продан', 'description': 'злой кот'}
        id_pet = adding_a_pet_by_id
        response = requests.post(url=BASE_URL + f'/{id_pet}', params=params)

        Response(response=response).assert_status_code(405).assert_message(id_pet)

    @pytest.mark.edit
    @pytest.mark.parametrize('adding_a_pet_by_id', ['with delete'], indirect=True)
    def test_put_correct(self, adding_a_pet_by_id):
        id_pet = adding_a_pet_by_id
        response = requests.put(url=BASE_URL, json=PetGenerator().set_pet_id(id_pet).set_name("Барсик").build())

        Response(response=response).assert_status_code(200).validate(Pet)

    @pytest.mark.skip("Нет обработки невалидного id")
    @pytest.mark.edit
    def test_put_incorrect_id(self):
        response = requests.put(url=BASE_URL,
                                json=PetGenerator().set_pet_id(-1).build())

        Response(response=response).assert_status_code(400)

    @pytest.mark.skip("Нет валидации на данных")
    @pytest.mark.edit
    @pytest.mark.parametrize('adding_a_pet_by_id', ['with delete'], indirect=True)
    def test_put_incorrect_validation(self, adding_a_pet_by_id):
        id_pet = adding_a_pet_by_id
        response = requests.put(url=BASE_URL,
                                json=PetGenerator().set_pet_id(id_pet).update_inner_value(['Имя'], 'кот').build())

        Response(response=response).assert_status_code(405)

    @pytest.mark.deletion
    @pytest.mark.parametrize('adding_a_pet_by_id', ['without delete'], indirect=True)
    def test_delete_correct(self, adding_a_pet_by_id):
        id_pet = adding_a_pet_by_id

        id_to_delete = f'/{id_pet}'
        response = requests.delete(url=BASE_URL + id_to_delete)

        Response(response=response).assert_status_code(200).assert_message(id_pet)

    @pytest.mark.skip("Нет проверки данных")
    @pytest.mark.deletion
    def test_delete_incorrect(self):

        id_to_delete = f'/{-1}'
        response = requests.delete(url=BASE_URL + id_to_delete)
        print(response)
        Response(response=response).assert_status_code(400)

    @pytest.mark.receiving
    @pytest.mark.parametrize("get_pets", ["by_id"], indirect=True)
    def test_get_by_id_correct(self, get_pets, common_setup_and_teardown_receiving):
        Response(response=get_pets(common_setup_and_teardown_receiving)).assert_status_code(200).validate(Pet)

    @pytest.mark.receiving
    @pytest.mark.parametrize("get_pets", ["by_id"], indirect=True)
    def test_get_by_id_incorrect(self, get_pets):
        Response(response=get_pets(-1)).assert_status_code(404)

    @pytest.mark.receiving
    @pytest.mark.parametrize('get_pets, status',
                             [('by_status', 'available'),
                              ('by_status', 'sold'),
                              ('by_status', 'pending')],
                             indirect=['get_pets'])
    def test_get_by_status_correct(self, get_pets, status, common_setup_and_teardown_receiving):
        Response(response=get_pets(status)).assert_status_code(200).validate(Pet)

    @pytest.mark.skip("Нет обработки невалидного статуса")
    @pytest.mark.receiving
    @pytest.mark.parametrize('get_pets, status',
                             [('by_status', 'продан'),
                              ('by_status', 'покормлен')],
                             indirect=['get_pets'])
    def test_get_by_status_incorrect(self, get_pets, status):
        Response(response=get_pets(status)).assert_status_code(400)
