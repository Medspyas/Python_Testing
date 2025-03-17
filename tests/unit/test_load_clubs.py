import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import loadClubs



def test_load_club_valid():
    clubs = loadClubs()
    assert isinstance(clubs, list)    
    for club in clubs:
        assert "name" in club
        assert "email" in club
        assert "points" in club


