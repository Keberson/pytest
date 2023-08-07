import pytest
from typing import List, Optional
from pydantic import BaseModel, ValidationError
from enum import StrEnum, auto
import requests
import json

ENDPOINT = 'https://petstore.swagger.io/v2/pet'


class StatusEnum(StrEnum):
    available = auto()
    pending = auto()
    sold = auto()


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photoUrls: List[str]
    tags: Optional[List[Tag]] = []
    status: Optional[StatusEnum] = None

    def __eq__(self, other):
        if not isinstance(other, Pet):
            raise TypeError("Некорректный операнд справа")

        self_dict = self.__dict__
        other_dict = other.__dict__

        return all([self_dict[field] == other_dict[field]
                    if field != 'id' or not (field == 'id' and (self.id is None or other.id is None)) else
                    True
                    for field in self_dict])


class PetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pet):
            tmp = obj.__dict__
            res: dict = {}

            for key in tmp:
                if tmp[key] is not None:
                    match key:
                        case 'category':
                            res[key] = obj.category.__dict__
                        case 'tags':
                            res[key] = [tag.__dict__ for tag in obj.tags]
                        case _:
                            res[key] = tmp[key]

            return res
        return json.JSONEncoder.default(self, obj)


@pytest.fixture()
def headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }


@pytest.fixture(scope="session")
def pets():
    return []


class TestPet:
    @pytest.mark.parametrize(
        'payload',
        [
            {
                'name': "doggie",
                'photoUrls': ["url"]
            },
            {
                'name': "new doggie",
                'photoUrls': ["url"],
                'category': {'id': 0, 'name': "string"},
                'tags': [{'id': 0, "name": "string"}],
                'status': "available"
            }
        ]
    )
    @pytest.mark.create
    def test_post_correct(self, headers, pets, payload):
        pet = Pet(**payload)
        serialized = json.dumps(pet, cls=PetEncoder)

        response = requests.post(
            ENDPOINT,
            data=serialized,
            headers=headers
        )

        assert response.status_code == 200

        try:
            got_pet = Pet(**json.loads(response.content))
            assert pet == got_pet

            pets.append(got_pet)
        except ValidationError:
            assert False

    @pytest.mark.create
    def test_post_incorrect(self, headers):
        response = requests.post(
            ENDPOINT,
            data={},
            headers=headers
        )

        assert response.status_code == 405

    @pytest.mark.edit
    def test_put(self):
        pass

    def test_get_find_by_status(self):
        pass

    def test_get_id_correct(self, pets):
        for pet in pets:
            response = requests.get(f'{ENDPOINT}/{pet.id}')
            assert response.status_code == 200

            got_pet = Pet(**json.loads(response.content))
            assert pet == got_pet

    @pytest.mark.parametrize(
        'payload',
        ['0', '-1', 'abd']
    )
    def test_get_id_incorrect(self, payload):
        response = requests.get(f'{ENDPOINT}/{payload}')
        assert response.status_code == 404

    def test_post_id_correct(self, pets):
        for pet in pets:
            params = {'name': 'Vasya', 'status': 'sold'}
            response = requests.post(f'{ENDPOINT}/{pet.id}', params=params)
            assert response.status_code == 200

    def test_delete_id_correct(self, pets):
        for pet in pets:
            response = requests.delete(f'{ENDPOINT}/{pet.id}')
            assert response.status_code == 200

            pets.remove(pet)

    @pytest.mark.parametrize(
        'payload',
        ['0', '-1', 'abd']
    )
    def test_delete_id_incorrect(self, payload):
        response = requests.delete(f'{ENDPOINT}/{payload}')

        assert response.status_code == 404
