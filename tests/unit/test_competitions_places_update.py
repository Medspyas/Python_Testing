import os
import sys

from utils import deduct_competitions_places

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_deduct_competitions_places():
    assert deduct_competitions_places(25, 5) == 20
