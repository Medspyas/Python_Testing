import os
import sys

from utils import validate_max_places_reservation

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_purchase_places_max_12():
    assert validate_max_places_reservation(12) is True


def test_purchase_places_more_than_12():
    assert validate_max_places_reservation(13) is False
