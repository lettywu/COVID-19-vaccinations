# imports
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, Response, render_template, jsonify

# initialize the flask app
app = Flask('BestVaccDist')

# route 1: hello world
# return a simple string
@app.route('/')
# create the controller
def home():
    return render_template('index.html')

@app.route('/covid_map')
def covid_map():
    return render_template('covid_map.html')

# route 5: accept the form submission and do something fancy with it
# load in the form data from the incoming request
# manipulate data into a format that we pass to our model
# Call app.run(debug=True) when python script is called
if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT", 8083)))
