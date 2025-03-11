import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from server import app, loadClubs




clubs = loadClubs()

email = clubs[0]["email"]


def showSummary_test(email, clubs):
    club = [club for club in clubs if club['email'] == email][0]
    return f"Welcome, {club['email']}"

def test_email_valid():    
    response = showSummary_test(email, clubs)
    assert response == f"Welcome, {email}"

def test_email_invalid():
    email = 'test@mail.com'
    response = showSummary_test(email, clubs)
    assert response == "enter email valid"

def test_email_empty():
    email = ''
    response = showSummary_test(email, clubs)
    assert response == "No email enter"   



