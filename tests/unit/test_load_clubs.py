import os
import sys

from server import loadClubs

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_load_club_valid():
    clubs = loadClubs()
    assert isinstance(clubs, list)
    for club in clubs:
        assert "name" in club
        assert "email" in club
        assert "points" in club
