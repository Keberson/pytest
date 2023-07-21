from abc import ABC, abstractmethod


class ApiRequest(ABC):
    def __init__(self, payload):
        self.__payload = payload

    TYPE = 'None'

    @abstractmethod
    def change_payload(self, payload):
        pass


class GetApiRequest(ApiRequest):
    TYPE = 'GET'

    def change_payload(self, payload):
        self.__payload = payload
