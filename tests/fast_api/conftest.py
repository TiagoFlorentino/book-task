import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def fast_api_test_client():
    return TestClient(app)
