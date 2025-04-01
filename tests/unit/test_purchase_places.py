import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils import purchase_places_validity







def test_purchase_places():
    result = purchase_places_validity(10, 10, 3)    
    assert result == "ok"

def test_purchase_places_too_many_places():
    result = purchase_places_validity(15, 5, 6)
    assert result == "not enough places"


def test_purchase_places_not_enough_points():
    result = purchase_places_validity(5, 10, 8)
    assert result == 'not enough points'

