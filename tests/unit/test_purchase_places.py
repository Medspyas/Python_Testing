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


def test_purchase_places(client):
    response = client.post('/purchasePlaces', data={
        "competition" : "Fall Classic",
        "club" : "Iron Temple",
        "places": "3"
    })
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data

def test_purchase_places_too_many_places(client):
    response = client.post('/purchasePlaces', data={
        "competition" : "Fall Classic",
        "club" : "Iron Temple",
        "places": "50"
    })
    assert b"Great-booking complete!" not in response.data


def test_purchase_places_not_enough_points(client):
    response = client.post('/purchasePlaces', data={
        "competition" : "Fall Classic",
        "club" : "Iron Temple",
        "places": "10"
    })
    assert b"Great-booking complete!" not in response.data
    
