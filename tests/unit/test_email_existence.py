import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils import find_club_email









def test_email_valid():    
    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co"},
        {"name": "Iron Temple", "email": "admin@irontemple.com"}
    ]
    club = find_club_email(clubs, "john@simplylift.co")
    assert club['name'] == "Simply Lift"

def test_email_invalid():    
    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co"}        
    ]
    club = find_club_email(clubs, "test@mail.com")
    assert club is None

def test_email_empty():    
    clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co"}        
    ]
    club = find_club_email(clubs, "")
    assert club is None



