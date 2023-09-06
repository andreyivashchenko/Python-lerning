from abc import ABC, abstractmethod
from accessify import protected


class ApiRequest(ABC):

    @property
    @abstractmethod
    def payload(self):
        pass

    @payload.setter
    @abstractmethod
    def payload(self, value):
        pass

    @property
    @abstractmethod
    def method(self):
        pass

    @protected
    @method.setter
    @abstractmethod
    def method(self, value):
        pass


class GetRequest(ApiRequest):
    def __init__(self, payload=''):
        self.method = "GET"
        self.payload = payload

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        self.__payload = value

    @property
    def method(self):
        return self.__METHOD

    @method.setter
    def method(self, value):
        self.__METHOD = value


class PostRequest(ApiRequest):
    def __init__(self, payload=''):
        self.method = "POST"
        self.payload = payload

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        self.__payload = value

    @property
    def method(self):
        return self.__METHOD

    @method.setter
    def method(self, value):
        self.__METHOD = value

