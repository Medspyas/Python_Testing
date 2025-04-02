import os
import sys

from utils import format_club_points

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_format_club_points():
    clubs = [
        {"name": "Simply Lift", "points": 13},
        {"name": "Iron Temple", "points": 4},
    ]
    result = format_club_points(clubs)
    assert result == [("Simply Lift", 13), ("Iron Temple", 4)]
