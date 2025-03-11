import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from server import app, loadClubs



def test_showSummary_valid():
    clubs = loadClubs()
    email = clubs[0]['email']
    with app.test_client() as client:
        response = client.post('/showSummary', data={"email": email})
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_showSummary_invalid():
    with app.test_client() as client:
        response = client.post('/showSummary', data={'email' : 'test@gmail.com'})
    assert response.status_code == 200
    assert b"Sorry, that email was not found" in response.data


def test_showSummary_empty():
    with app.test_client() as client:
        response = client.post('/showSummary', data={'email' : ''})
    assert response.status_code == 200
    assert b"Please enter an email" in response.data