from app import app
from flask import render_template
import json

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/viz')
def viz():
    return render_template("viz.html")


# example data service routing
@app.route('/dataservices/<service>')
def dataservices(service):
    if service == 'pitchers':
        return json.dumps(
            [{"pitcher":"some guy"},
             {"pitcher":"some other guy"},
             {"pitcher":"the last guy"}])

    elif service == 'teams':
        return json.dumps(
            [{"team":"baltimore orioles"},
             {"team":"san francisco giants"},
             {"team":"washington nationals"}])
