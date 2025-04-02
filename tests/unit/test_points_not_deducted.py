import os
import sys

from utils import deduct_points

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_deduct_points():
    assert deduct_points(10, 3) == 7
