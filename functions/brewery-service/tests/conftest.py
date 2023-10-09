from fastapi.testclient import TestClient
import pytest
from app import create_app
from google.cloud.firestore_v1.types import WriteResult


class MockDocument:
    """Used to test Firestore documents"""

    def __init__(self):
        self.data = {}

    def set(self, data: dict) -> WriteResult:
        return WriteResult()


class MockFirestoreCollection:
    """Mocks a firestore collection for testing"""

    def __init__(self) -> None:
        self.docs = []

    def stream(self) -> list:
        return self.docs

    def document(self, id: str) -> MockDocument:
        return MockDocument()


class MockFirestoreClient:
    """Mocks calls to firestore for testing"""

    def __init__(self) -> None:
        self.docs = []

    def collection(self) -> MockFirestoreCollection:
        return MockFirestoreCollection()


@pytest.fixture
def test_api_client(mock_firestore_collection) -> TestClient:
    """Create a FastAPI test client"""
    app = create_app(firestore_collection=mock_firestore_collection)
    client = TestClient(app)

    yield client


@pytest.fixture
def mock_firestore_client() -> MockFirestoreClient:
    yield MockFirestoreClient()


@pytest.fixture
def mock_firestore_collection() -> MockFirestoreCollection:
    yield MockFirestoreCollection()
