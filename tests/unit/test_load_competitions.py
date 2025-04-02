import os
import sys

from server import loadCompetitions

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_load_competition_valid():
    competitions = loadCompetitions()
    assert isinstance(competitions, list)
    for competition in competitions:
        assert "name" in competition
        assert "date" in competition
        assert "numberOfPlaces" in competition
