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

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/data_cleaning')
def data_cleaning():
    return render_template('data_cleaning.html')

@app.route('/vac-mask-cleaning')
def vac_mask_cleaning():
    return render_template('jesse_data_cleaning.html')

@app.route('/population-vaccine-cleaning')
def population_mask_cleaning():
    return render_template('data_cleaning_population_merge_to_vaccine_letty.html')

@app.route('/scrapped-data-cleaning')
def scrapped_data_cleaning():
    return render_template('data_cleaning_scrapped-vaccine-data-combine-california-letty.html')

@app.route('/vaccine-allocation-cleaning')
def vaccine_allocation_cleaning():
    return render_template('data_cleaning_vaccine_allocations_per_state_letty.html')

@app.route('/hospital-data-cleaning')
def hospital_data_cleaning():
    return render_template('Clean-Hospital-by-County.html')

@app.route('/EDA')
def EDA():
    return render_template('EDA.html')

@app.route('/map_page')
def covid_map():
    return render_template('map_page.html')

# route 5: accept the form submission and do something fancy with it
# load in the form data from the incoming request
# manipulate data into a format that we pass to our model
# Call app.run(debug=True) when python script is called
if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT", 8083)))
