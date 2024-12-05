# this is the "web_app/routes/drinks_challenge_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.drinks_challenge import fetch_drinks_json

drinks_challenge_routes = Blueprint("drinks_challenge_routes", __name__)

@drinks_challenge_routes.route("/drinks_challenge")
def drinks_challenge():
    print("DRINKS CHALLENGE...")

    try:
        data = fetch_drinks_json()

        #flash("Fetched Latest Drinks Challenge Data!", "success")
        return render_template("drinks_challenge.html",
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        #flash("Drinks Challenge Data Error. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@drinks_challenge_routes.route("/api/drinks_challenge.json")
def drinks_challenge_api():
    print("DRINKS CHALLENGE (API)...")

    try:
        data = fetch_drinks_json()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Drinks Challenge Data Error. Please try again."}, 404