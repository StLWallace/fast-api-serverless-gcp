from models.breweries import Brewery
import pytest


@pytest.fixture()
def fake_brewery_record() -> Brewery:
    yield Brewery(
        **{
            "name": "Test Brewery",
            "location": {"city": "Fake City", "state": "Fake State", "zipcode": "123"},
            "contact": {"phone_number": "000-000-0000", "email": "fake@fake.com"},
        }
    )


def test_breweries_post(test_api_client, fake_brewery_record):
    """Confirm response from post endpoint"""
    app = test_api_client

    response = app.post(
        "/breweries/",
        content=fake_brewery_record.model_dump_json(),
        headers={"Content-Type": "application/json"},
    )

    assert response.json() == fake_brewery_record.model_dump()
