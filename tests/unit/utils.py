


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

