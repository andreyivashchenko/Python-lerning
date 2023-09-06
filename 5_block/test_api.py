from Api import *
import pytest


@pytest.fixture(scope="class")
def created_requests():
    return {'GET': GetRequest(payload="Empty"), 'POST': PostRequest(payload="Empty")}


class TestApi:
    def test_get_request(self, created_requests):
        assert created_requests['GET'].method == 'GET'
        assert created_requests['GET'].payload == "Empty"

    def test_post_request(self, created_requests):
        assert created_requests['POST'].method == 'POST'
        assert created_requests['POST'].payload == "Empty"

    @pytest.mark.parametrize(
        "payload", ["Тестовые данные", 11111, '']
    )
    def test_change_payload_get(self, created_requests, payload):
        created_requests['GET'].payload = payload

        assert created_requests['GET'].payload == payload

    @pytest.mark.parametrize(
        "payload", ["Тестовые данные", 11111, '']
    )
    def test_change_payload_post(self, created_requests, payload):
        created_requests['POST'].payload = payload

        assert created_requests['POST'].payload == payload