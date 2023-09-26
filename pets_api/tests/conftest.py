import pytest
import requests
from pets_api.configuration import BASE_URL
from pets_api.src.generators.pet import PetGenerator


@pytest.fixture(scope="class")
def common_setup_and_teardown_receiving():
    statuses = ("available", "sold", "pending")
    pet_ids = []
    for status in statuses:
        pet_ids.append(requests.post(url=BASE_URL, json=PetGenerator().set_status(status).build()).json()["id"])
    obj_to_send = PetGenerator().build()
    id_pet = requests.post(url=BASE_URL, json=obj_to_send).json()['id']
    yield id_pet
    requests.delete(url=BASE_URL + f'/{id_pet}')
    for id in pet_ids:
        requests.delete(url=BASE_URL + f'/{id}')


def _get_pet_by_id(id_pet):
    test_item = f'/{id_pet}'
    resp = requests.get(url=BASE_URL + test_item)
    return resp


def _get_pet_by_status(status):
    resp = requests.get(url=BASE_URL + "/findByStatus", params=status)
    return resp


@pytest.fixture(scope='class')
def get_pets(request):
    params = request.param

    if params == "by_id":
        return _get_pet_by_id
    elif params == "by_status":
        return _get_pet_by_status
    else:
        raise ValueError("Неверный параметр")


@pytest.fixture(scope='function')
def adding_a_pet_by_id(request):
    params = request.param

    id_pet = requests.post(url=BASE_URL, json=PetGenerator().build()).json()['id']

    yield id_pet

    if params == "with delete":
        requests.delete(url=BASE_URL + f'/{id_pet}')
    elif params == "without delete":
        pass
