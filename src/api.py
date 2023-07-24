from accessify import protected
from abc import ABC, abstractmethod


class ApiRequest(ABC):
    def __init__(self, payload=''):
        self.__payload = payload

    TYPE = 'None'

    def get_payload(self):
        return self.__payload

    @protected
    def set_payload(self, payload):
        self.__payload = payload

    @abstractmethod
    def change_payload(self, payload=''):
        pass


class GetApiRequest(ApiRequest):
    TYPE = 'GET'

    def change_payload(self, payload=''):
        self.set_payload(payload)


class PostApiRequest(ApiRequest):
    TYPE = 'POST'

    def change_payload(self, payload=''):
        self.set_payload(payload)


class DeleteApiRequest(ApiRequest):
    TYPE = 'DELETE'

    def change_payload(self, payload=''):
        self.set_payload(payload)
