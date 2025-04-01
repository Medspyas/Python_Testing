


def find_club_email(clubs, email):
    if not email:
        return None
    return next((c for c in clubs if c['email'] == email), None)