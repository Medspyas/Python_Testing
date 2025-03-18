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


def test_book_past_competition(client):
    response = client.post('/purchasePlaces', data={
        "competition" : "Spring Festival",
        "club" : "Simply Lift",
        "places": "5"
    })

   
    assert response.status_code == 200
    assert b"Great-booking complete!" not in response.data