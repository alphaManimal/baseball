from app import app
from flask import render_template
from flask import request
import json
import models

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/viz')
def viz():
    return render_template("viz.html")


# example data service routing
@app.route('/dataservices/<service>')
def dataservices(service):
    # a test
    if service == 'tables':
        return models.dataserver(service)
