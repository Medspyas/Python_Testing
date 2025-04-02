import os
import sys

from utils import is_competition_not_in_past

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


def test_book_past_competition_valid():
    assert is_competition_not_in_past("2025-12-31 12:30:00") is True


def test_book_past_competition_not_valid():
    assert is_competition_not_in_past("2024-12-31 12:30:00") is False
