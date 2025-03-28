import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import pytest
from server import app, competitions , clubs, loadClubs, loadCompetitions






def test_places_deducted_after_booking():
    with app.test_client() as client:    
        competitions = loadCompetitions()
        club_name = 'Sonics'
        competition_name = 'Summer Tournament'
        place_to_book = 2    
        competition = next(c for c in competitions if c['name'] == competition_name)

        initial_places = int(competition['numberOfPlaces'])
        

        response = client.post('/purchasePlaces', data={
            'club': club_name,
            'competition': competition_name,
            'places': str(place_to_book)
        })

        competitions_after = loadCompetitions()
        competition_after = next(c for c in competitions_after if c['name'] == competition_name)
        places_after = int(competition_after['numberOfPlaces'])


        assert response.status_code == 200    
        assert places_after == initial_places - place_to_book

