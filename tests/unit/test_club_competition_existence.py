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

    
    
def test_book_valid(client):
    response = client.get('/book/Spring Festival/Simply Lift')
    assert response.status_code == 200
    assert b'Spring Festival' in response.data




