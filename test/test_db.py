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


class TestDB:
    @pytest.mark.parametrize(
        'payload',
        [
            {
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
            }
        ]
    )
    def test_create_user(self, db, payload):
        db.create_user(payload)

    def test_get_info_user(self, db):
        pass

    def test_update_user(self, db):
        pass

    def test_delete_user(self, db):
        pass
