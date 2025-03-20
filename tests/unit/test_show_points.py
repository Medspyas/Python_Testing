import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app, loadClubs
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client




def test_show_points(client):  
    response = client.get('/points')

    assert response.status_code == 200 

    clubs = loadClubs()
    for club in clubs:
        assert club['name'].encode() in response.data
        assert str(club['points']).encode() in response.data