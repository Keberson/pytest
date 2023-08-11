import pytest
from pydantic import BaseModel, ValidationError, HttpUrl
from typing import Optional

from src.db import *

DATABASE_SETTINGS = {
    'host': 'psql-mock-database-cloud.postgres.database.azure.com',
    'port': 5432,
    'user': 'rzpdhletunsxxewhttixfihc@psql-mock-database-cloud',
    'password': 'noenhpbguefolkrnqmvwhypz',
    'dbname': 'booking1691643768927avbbmklqfugabxqi'
}


class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    full_name: str
    job_title: str
    job_type: str
    phone: str
    email: str
    image: HttpUrl
    country: str
    city: str
    onboarding_completion: int


@pytest.fixture(scope="session")
def db() -> DB:
    """
    Фикстура для установления подключения к базе данных
    :return: объект класса DB
    """
    _db = DB(DATABASE_SETTINGS)
    _db.connect()

    return _db


@pytest.fixture(scope="session")
def users() -> list[tuple[dict, dict]]:
    """
    Фикстура для получения тестовых данных
    :return: список кортежей типа (User в формате dict, ожидаемый ответ в формате dict)
    """
    return [
        ({
             "id": 8008080,
             "first_name": "John",
             "last_name": "Doe",
             "full_name": "John Doe",
             "job_title": "Software Engineer",
             "job_type": "Full-time",
             "phone": "123-456-7890",
             "email": "johndoe@example.com",
             "image": "https://example.com/images/johndoe.jpg",
             "country": "USA",
             "city": "New York",
             "onboarding_completion": 80
         }, {'all': 1, 'update': 2, 'delete': 2}),
        ({
             "id": 8998989,
             "first_name": "Jane",
             "last_name": "Smith",
             "full_name": "Jane Smith",
             "job_title": "Marketing Manager",
             "job_type": "Part-time",
             "phone": "987-654-3210",
             "email": "janesmith@example.com",
             "image": "https://example.com/images/janesmith.jpg",
             "country": "Canada",
             "city": "Toronto",
             "onboarding_completion": 100
         }, {'all': 1}),
        ({
             "id": 12345678,
             "first_name": "David",
             "last_name": "Johnson",
             "full_name": "David Johnson",
             "job_title": "Project Manager",
             "job_type": "Full-time",
             "phone": "555-123-4567",
             "email": "davidjohnson@example.com",
             "image": "https://example.com/images/davidjohnson.jpg",
             "country": "Australia",
             "city": "Sydney",
             "onboarding_completion": 50
         }, {'all': 1}),
        ({
             "id": 8008080,
             "first_name": "John",
             "last_name": "Doe",
             "full_name": "John Doe",
             "job_title": "Software Engineer",
             "job_type": "Full-time",
             "phone": "123-456-7890",
             "email": "johndoe@example.com",
             "image": "https://example.com/images/johndoe.jpg",
             "country": "USA",
             "city": "New York",
             "onboarding_completion": 80
         }, {'create': 0, 'all': -1})
    ]


@pytest.fixture(scope="session", autouse=True)
def clear_db(db, users) -> None:
    """
    Авто фикстура для очистки БД после тестов
    :param db: фикстура БД
    :param users: фикстура с тестовыми данными
    """
    yield
    for row in users:
        user = row[0]
        expect = row[1]

        if expect['all'] == -1:
            continue

        db.delete_user(user['id'])


class TestDB:
    def test_create_user(self, db, users):
        for row in users:
            user = row[0]
            expect = row[1]
            expect = expect['create'] if 'create' in expect else expect['all']

            if expect == -1:
                continue

            assert db.create_user(user) == expect

    def test_get_info_user(self, db, users):
        for row in users:
            user = row[0]
            expect = row[1]
            expect = expect['get'] if 'get' in expect else expect['all']

            if expect == -1:
                continue

            response = db.get_info_user(user['id'])

            assert response is not None

            try:
                User(**response)
            except ValidationError:
                assert False

            assert [user[key] == response[key] if key in response else False for key in user]

    def test_update_user(self, db, users):
        for row in users:
            user = row[0]
            expect = row[1]
            expect = expect['update'] if 'update' in expect else expect['all']

            if expect == -1:
                continue

            to_update = {'first_name': 'Максим', 'onboarding_completion': 5}

            assert db.update_user(user['id'], to_update) == expect

    def test_delete_user(self, db, users):
        for row in users:
            user = row[0]
            expect = row[1]
            expect = expect['delete'] if 'delete' in expect else expect['all']

            if expect == -1:
                continue

            assert db.delete_user(user['id']) == expect
