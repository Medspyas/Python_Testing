import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app




def test_purchase_places_max_12():
    with app.test_client() as client:
        competition_name = "Fall Classic"
        club_name = "Simply Lift"

        response = client.post('/purchasePlaces', data={
            'competition': competition_name,
            'club': club_name,
            'places': '13',
        }, follow_redirects=True)

        assert response.status_code == 200
        assert b"Cannot book more than 12 places per reservation" in response.data