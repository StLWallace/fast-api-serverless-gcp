from fastapi.testclient import TestClient
import pytest
from app import create_app


@pytest.fixture()
def test_api_client() -> TestClient:
    """Create a FastAPI test client"""
    client = TestClient(create_app())

    yield client
