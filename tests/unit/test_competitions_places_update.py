import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils import deduct_competitions_places




def test_deduct_competitions_places():
    assert deduct_competitions_places(25, 5) == 20

