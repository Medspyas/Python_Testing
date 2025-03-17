import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app




def test_purchase_places_valid():
    with app.test_client() as client:
        competition_name = "Spring Festival"
        club_name = "Simply Lift"

        response = client.post('/purchasePlaces', data={
            'competition': competition_name,
            'club': club_name,
            'places': '2',
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data


def test_purchase_places_too_many_places():
    with app.test_client() as client:
        competition_name = "Spring Festival"
        club_name = "Simply Lift"

        response = client.post('/purchasePlaces', data={
            'competition': competition_name,
            'club': club_name,
            'places': '1000',
        }, follow_redirects=True)


        response_text = response.data.decode().strip()        
        assert response.status_code == 200
        assert "Not enough places available" in response_text

def test_purchase_places_not_enough_points():
    with app.test_client() as client:
        competition_name = "Spring Festival"
        club_name = "Iron Temple"       


        response = client.post('/purchasePlaces', data={
            'competition': competition_name,
            'club': club_name,
            'places': '10',
        }, follow_redirects=True)
       

        response_text = response.data.decode().strip()              
        assert response.status_code == 200
        assert "Not enough points available" in response_text


def test_purchase_places_invalid_number():
    with app.test_client() as client:
        competition_name = "Spring Festival"
        club_name = "Simply Lift"

        response = client.post('/purchasePlaces', data={
            'competition': competition_name,
            'club': club_name,
            'places': '0',
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b"Invalid number" in response.data