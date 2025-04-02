import json
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()


def saveClubs(clubs):
    # Permet de mettre à jour les points après reservation.
    with open("clubs.json", "w") as f:
        json.dump({"clubs": clubs}, f, indent=4)


def saveCompetitions(competitions):
    # Permet de mettre à jour les places disponibles après reservation.
    with open("competitions.json", "w") as f:
        json.dump({"competitions": competitions}, f, indent=4)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    # Permet de s'authentifier grâce à une adresse e-mail
    # S'assure qu'elle affiche un message d'erreur de fausses informations
    email = request.form.get("email")
    if not email:
        return "Please enter an email."

    club = next((club for club in clubs if club["email"] == email), None)

    if club is None:
        return "Sorry, that email was not found."
    else:
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    # Affiche les informations du club ainsi qu'une liste de competitions disponible.
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    # Permet de valider l'opération de reservation de compétition.
    # Elle verifie:
    #   - qu'on peut pas reserver plus de point que disponible.
    #   - qu'on peut pas reserver plus de point a 12 point.
    #   - qu'on peut pas reserver une competition à une date anterieur.
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    club_points = int(club["points"])
    competition_places = int(competition["numberOfPlaces"])
    competition_date = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
    currente_date = datetime.now()

    def return_message(msg):
        flash(msg)
        return render_template("welcome.html", club=club, competitions=competitions)

    if competition_date < currente_date:
        return return_message("You cannot book a place for a past competition")

    if placesRequired > 12:
        return return_message("Cannot book more than 12 places per reservation")

    if placesRequired > competition_places:
        return return_message("Not enough places available")

    if placesRequired > club_points:
        return return_message("Not enough points available")

    competition["numberOfPlaces"] = str(competition_places - placesRequired)
    club["points"] = str(club_points - placesRequired)
    saveClubs(clubs)
    saveCompetitions(competitions)
    flash("Great-booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display


@app.route("/points")
def showPoints():
    # Affiche une liste des clubs existants ainsi que leur points.
    return render_template("points.html", clubs=clubs)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
