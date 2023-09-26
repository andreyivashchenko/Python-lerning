import pytest
import requests

from pets_api.src.baseclasses.response import Response
from pets_api.src.schemas.pet import Pet
from pets_api.src.generators.pet import PetGenerator
from pets_api.configuration import BASE_URL


class TestPetsApi:
    @pytest.mark.create
    def test_post_new_pet(self):
        response = requests.post(url=BASE_URL, json=PetGenerator().build())

        Response(response=response).assert_status_code(200).validate(Pet)

        id_to_delete = f'{response.json()["id"]}'
        requests.delete(url=BASE_URL + id_to_delete)

    @pytest.mark.parametrize('adding_or_removing_a_pet_by_id', ['with delete'], indirect=True)
    @pytest.mark.create
    def test_post_existing_pet(self, adding_or_removing_a_pet_by_id):
        params = {'name': 'Vasya', 'status': 'sold'}
        id_pet = adding_or_removing_a_pet_by_id
        post_resp = requests.post(url=BASE_URL + f'/{id_pet}', params=params)

        Response(response=post_resp).assert_status_code(200).assert_message(id_pet)

    @pytest.mark.edit
    @pytest.mark.parametrize('adding_or_removing_a_pet_by_id', ['with delete'], indirect=True)
    def test_put(self, adding_or_removing_a_pet_by_id):
        id_pet = adding_or_removing_a_pet_by_id
        put_resp = requests.put(url=BASE_URL, json=PetGenerator().set_pet_id(id_pet).set_name("Петрович").build())

        Response(response=put_resp).assert_status_code(200).validate(Pet)

    @pytest.mark.delete
    @pytest.mark.parametrize('adding_or_removing_a_pet_by_id', ['without delete'], indirect=True)
    def test_delete(self, adding_or_removing_a_pet_by_id):
        id_pet = adding_or_removing_a_pet_by_id

        id_to_delete = f'/{id_pet}'
        response = requests.delete(url=BASE_URL + id_to_delete)

        Response(response=response).assert_status_code(200).assert_message(id_pet)

    @pytest.mark.receiving
    @pytest.mark.parametrize("get_pets", ["by_id"], indirect=True)
    def test_get_by_id(self, get_pets, common_setup_and_teardown_receiving):
        Response(response=get_pets(common_setup_and_teardown_receiving)).assert_status_code(200).validate(Pet)

    @pytest.mark.receiving
    @pytest.mark.parametrize('get_pets, status',
                             [('by_status', 'available'),
                              ('by_status', 'sold'),
                              ('by_status', 'pending')],
                             indirect=['get_pets'])
    def test_get_by_status(self, get_pets, status, common_setup_and_teardown_receiving):
        Response(response=get_pets(status)).assert_status_code(200).validate(Pet)
