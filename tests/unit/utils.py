from datetime import datetime


def find_club_email(clubs, email):
    if not email:
        return None
    return next((c for c in clubs if c['email'] == email), None)

def purchase_places_validity(club_points, competitions_places, places_required):
    if places_required > competitions_places:
        return "not enough places"
    if places_required > club_points:
        return "not enough points"
    return "ok"

def validate_max_places_reservation(places_required, max_points=12):
    return places_required <= max_points


def is_competition_not_in_past(date_string, format="%Y-%m-%d %H:%M:%S"):
    competition_date = datetime.strptime(date_string, format)
    return competition_date > datetime.now()

def deduct_points(club_points, places_resreved):
    return club_points - places_resreved

def deduct_competitions_places(competition_places, place_reserved):
    return competition_places - place_reserved

def find_club_by_name(clubs, name):
    return next((c for c in clubs if c['name'] == name), None)

def find_club_by_compeition(compeitions, name):
    return next((c for c in compeitions if c['name'] == name), None)