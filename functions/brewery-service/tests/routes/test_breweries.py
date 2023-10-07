from routes.breweries import create_brewery
from models.breweries import Brewery


def test_breweries_post(test_api_client):
    """Confirm response from post endpoint"""
    app = test_api_client
    test_brewery = Brewery(
        **{
            "name": "Test Brewery",
            "location": {"city": "Fake City", "state": "Fake State", "zipcode": "123"},
            "contact": {"phone_number": "000-000-0000", "email": "fake@fake.com"},
        }
    )

    response = app.post(
        "/breweries/",
        data=test_brewery.model_dump_json(),
        headers={"Content-Type": "application/json"},
    )

    assert response.json() == test_brewery.dict()


def test_create_brewery():
    """Test underlying function"""
    pass