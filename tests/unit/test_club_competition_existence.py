import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils import find_club_by_name, find_club_by_compeition



def test_book_valid_club_and_competition():
    clubs = [{"name": "Simply Lift"}, {"name" : "Iron Temple"}]
    competitions = [{"name": "Spring Festival"}, {"name": "Fall Classic"}]

    club = find_club_by_name(clubs, "Simply Lift")
    competiton = find_club_by_compeition(competitions, "Spring Festival")

    assert club["name"] == "Simply Lift"
    assert competiton["name"] == "Spring Festival"

def test_club_does_not_exist():
    clubs = [{"name" : "Iron Temple"}]

    club = find_club_by_name(clubs, "No Club")
    assert club is None


def test_competition_does_not_exist():    
    competitions = [{"name": "Fall Classic"}]
    competiton = find_club_by_compeition(competitions, "No Competition")

    assert competiton is None






