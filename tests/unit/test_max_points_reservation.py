import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pytest
from server import app




@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_purchase_places_max_12(client):
    response = client.post('/purchasePlaces', data={
        "competition" : "Spring Festival",
        "club" : "Iron Temple",
        "places": "13"
    })
    assert response.status_code == 200
    assert b"Great-booking complete!"  not in response.data