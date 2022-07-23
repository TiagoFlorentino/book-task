import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def fast_api_test_client():
    return TestClient(app)


@pytest.fixture
def input_get_book_list():
    return [
        {"title": "BOOK_1", "status": "AVAILABLE"},
        {"title": "BOOK_2", "status": "RENTED"},
        {"title": "BOOK_3", "status": "DISCONTINUED"},
    ]


@pytest.fixture
def output_get_book_list():
    return [
        {"id": 1, "title": "BOOK_1", "status": "AVAILABLE", "renter_id": None},
        {"id": 2, "title": "BOOK_2", "status": "RENTED", "renter_id": None},
        {"id": 3, "title": "BOOK_3", "status": "DISCONTINUED", "renter_id": None},
    ]


@pytest.fixture
def input_status_book_list():
    return [
        {"title": "BOOK_1", "status": "RENTED", "renter_id": 1},
        {"title": "BOOK_2", "status": "DISCONTINUED", "renter_id": None},
    ]


@pytest.fixture
def output_status_book_list():
    return [
        {"id": 1, "title": "BOOK_1", "status": "AVAILABLE", "renter_id": None},
        {"id": 2, "title": "BOOK_2", "status": "AVAILABLE", "renter_id": None},
    ]


@pytest.fixture
def input_book_renting_queries():
    return [
        "INSERT INTO clients (name, active) VALUES ('ANDRE JOSE', 1)",
        "INSERT INTO clients (name, active) VALUES ('MANUEL RODRIGO', 1)",
        "INSERT INTO books (title, status) VALUES ('SOME BOOK 42', 'AVAILABLE')",
    ]


@pytest.fixture
def input_get_campaign_list():
    return [
        {"name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
        {"name": "CAMPAIGN_2", "slogan": "SLOGAN_B", "partner_id": 1},
    ]


@pytest.fixture
def output_get_campaign_list():
    return [
        {"id": 1, "name": "CAMPAIGN_1", "slogan": "SLOGAN_A", "partner_id": 1},
        {"id": 2, "name": "CAMPAIGN_2", "slogan": "SLOGAN_B", "partner_id": 1},
    ]
