import pytest
import requests

from pets_api.src.baseclasses.response import Response
from pets_api.src.schemas.pet import Pet
from pets_api.src.generators.pet import Pet_generator
from pets_api.configuration import BASE_URL


class TestPetsApi:
    @pytest.mark.create
    def test_post_new_pet(self):
        resp = requests.post(url=BASE_URL, json=Pet_generator().build())
        Response(response=resp).assert_status_code(200).validate(Pet)
        requests.delete(url=BASE_URL + f'{resp.json()["id"]}')

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
