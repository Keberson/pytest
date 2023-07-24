import pytest

from src.api import *


class TestApi:
    @pytest.fixture(scope='class')
    def get_request(self) -> GetApiRequest:
        return GetApiRequest(payload='Init')

    @pytest.fixture(scope='class')
    def post_request(self) -> PostApiRequest:
        return PostApiRequest(payload='Init')

    @pytest.fixture(scope='class')
    def delete_request(self) -> DeleteApiRequest:
        return DeleteApiRequest(payload='Init')

    def test_get_type(self, get_request):
        assert get_request.TYPE == 'GET'

    def test_post_type(self, post_request):
        assert post_request.TYPE == 'POST'

    def test_delete_type(self, delete_request):
        assert delete_request.TYPE == 'DELETE'

    @pytest.mark.parametrize(
        'payload',
        ['New post payload', '', 1234]
    )
    def test_get_payload(self, get_request, payload):
        get_request.change_payload(payload=payload)

        assert get_request.get_payload() == payload

    @pytest.mark.parametrize(
        'payload',
        ['New post payload', '', 1234]
    )
    def test_post_payload(self, post_request, payload):
        post_request.change_payload(payload=payload)

        assert post_request.get_payload() == payload

    @pytest.mark.parametrize(
        'payload',
        ['New post payload', '', 1234]
    )
    def test_delete_payload(self, delete_request, payload):
        delete_request.change_payload(payload=payload)

        assert delete_request.get_payload() == payload
