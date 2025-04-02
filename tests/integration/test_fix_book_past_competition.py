import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app


def test_book_past_competition():
    with app.test_client() as client:
        competition_name = "Spring Festival"
        club_name = "Simply Lift"

        response = client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": "6",
            },
            follow_redirects=True,
        )

        assert response.status_code == 200
        assert b"You cannot book a place for a past competition" in response.data
