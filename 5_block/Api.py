from abc import ABC, abstractmethod
from accessify import protected


class ApiRequest(ABC):
    def __init__(self, payload=''):
        self.__METHOD = None
        self.__payload = payload

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    @abstractmethod
    def payload(self, payload=''):
        pass

    @property
    def method(self):
        return self.__METHOD

    @protected
    @method.setter
    def method(self, method):
        self.__METHOD = method


class GetRequest(ApiRequest):
    def __init__(self, payload=None):
        super().__init__()
        self._ApiRequest__payload = payload
        self.method = "GET"

    @ApiRequest.payload.setter
    def payload(self, payload=''):
        self._ApiRequest__payload = payload


class PostRequest(ApiRequest):
    def __init__(self, payload=None):
        super().__init__()
        self._ApiRequest__payload = payload
        self.method = "POST"

    @ApiRequest.payload.setter
    def payload(self, payload=''):
        self._ApiRequest__payload = payload


if __name__ == "__main__":
    get = GetRequest("Гет запрос")
    post = PostRequest('Пост запрос')
    print(get.method, get.payload, post.method, post.payload)
    get.payload = "Гет ответ"
    post.payload = 'Пост ответ'
    print(get.method, get.payload, post.method, post.payload)

