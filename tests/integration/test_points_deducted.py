import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app, loadClubs


def test_points_deducted():

    club_name = "Simply Lift"
    competition_name = "Fall Classic"
    clubs = loadClubs()
    club = next(c for c in clubs if c["name"] == club_name)
    initial_points = int(club["points"])
    place_to_book = 3
    with app.test_client() as client:
        response = client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": str(place_to_book),
            },
        )

        clubs_after_purchase = loadClubs()
        club_after_purchase = next(
            c for c in clubs_after_purchase if c["name"] == club_name
        )
        points_after_purchase = int(club_after_purchase["points"])

        assert response.status_code == 200
        assert b"Great-booking complete!" in response.data

        assert points_after_purchase == initial_points - place_to_book
