import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app
import pytest 




@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client




def test_email_valid(client):    
    response = client.post('/showSummary', data={'email' : 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome' in response.data 

def test_email_invalid(client):    
    response = client.post('/showSummary', data={'email' : 'test@mail.com'})
    assert response.status_code == 200
    assert b"Welcome, test@mail.com" not in response.data

def test_email_empty(client):    
    response = client.post('/showSummary', data={'email' : ''})
    assert response.status_code == 200
    assert b"Please enter your secretary email to continue:" in response.data



