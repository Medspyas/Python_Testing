
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from utils import deduct_points



def test_deduct_points():
    assert deduct_points(10, 3) == 7



    

