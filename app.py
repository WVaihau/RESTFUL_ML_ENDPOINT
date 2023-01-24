
"""
simple python flask application for MLOPS COURSE
"""

##########################################################################
## Imports
##########################################################################

import os

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify

import controller as ctrl

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/classify")
def ml_classifier():
    """
    Return a prediction of what the input image can be with its accuracy
    """
    model = ctrl.load_model()

    parse_img = ctrl.parse_query(request.args["img"])

    y_pred = model.predict(parse_img)
    
    return jsonify({"prediction": ctrl.get_class(y_pred), "accuracy": ctrl.get_score(y_pred)})


##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()