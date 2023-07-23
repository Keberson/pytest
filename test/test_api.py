import pytest

from src.api import *


def test_type():
    get_request = GetApiRequest(payload='Init')

    assert get_request.TYPE == 'GET'

    post_request = PostApiRequest(payload='Init')

    assert post_request.TYPE == 'POST'

    delete_request = DeleteApiRequest(payload='Init')

    assert delete_request.TYPE == 'DELETE'

# def test_payload(request):
