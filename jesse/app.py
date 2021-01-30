# imports
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
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

@app.route('/data-cleaning-main')
def data_cleaning_main():
    return render_template('1_Data_Cleaning.html')

@app.route('/eda-main')
def eda_main():
    return render_template('2_EDA.html')

@app.route('/modeling-main')
def modeling_main():
    return render_template('3_Modeling.html')

@app.route('/folium-main')
def folium_main():
    return render_template('4_Folium.html')

@app.route('/prediction-conclusion-main')
def prediction_conclusion_main():
    return render_template('5_Predictions_and_Conclusions.html')

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

@app.route('/case-mask-eda')
def case_mask_eda():
    return render_template('Mask_Use_EDA.html')

@app.route('/hospital-beds-eda')
def hospital_beds_eda():
    return render_template('HospitalBeds_EDAgraphs_countybycounty.html')

@app.route('/vaccine-state-eda')
def vaccine_state_eda():
    return render_template('EDA_latest_vaccine_per_state_letty.html')

@app.route('/vaccine-administration-california')
def vaccine_administration_california():
    return render_template('EDA-scrapped-california-vaccine-letty.html')

@app.route('/covid-density-eda')
def covid_density_eda():
    return render_template('EDA-Hospital-by-County-Rahul.html')

@app.route('/EDA')
def EDA():
    return render_template('EDA.html')

@app.route('/tensorflow-lstm-model')
def tensorflow_lstm_model():
    return render_template('Feature_Engineering_And_Modeling.html')

@app.route('/arima-model')
def arima_model():
    return render_template('ARIMA_model.html')

@app.route('/sarimax-model')
def sarimax_model():
    return render_template('SARIMAX_model.html')

@app.route('/Modeling')
def Modeling():
    return render_template('Modeling.html')

@app.route('/folium-time-series')
def folium_time_series():
    return render_template('Folium.html')

@app.route('/map_tutorial')
def map_tutorial():
    return render_template('map_tutorial.html')

@app.route('/map_page')
def covid_map():
    return render_template('map_page.html')

@app.route('/get_predictions')
def get_predictions():
    return render_template('get_predictions.html')

@app.route('/submit', methods=['POST', 'GET'])
def make_predictions():
#    user_input = request.form.get('county')
#    counties_df = pd.read_csv('../clean_data/counties_models.csv')
#    counties_df['date'] = pd.to_datetime(counties_df['date'])
#    counties_df.set_index(['county', 'date'], inplace = True)
#    selected_df = counties_df.loc[user_input]
#    features = ['hospitalized_covid_patients']
#    X = selected_df[features]
#    y = selected_df[['7dayrollingavg_newlyconfirmed']].values
#    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = False, test_size = 0.15)
    # scale our data
#    mms = MinMaxScaler()
#    X_train_sc = mms.fit_transform(X_train)
#    X_test_sc = mms.transform(X_test)
#    new_model = load_model(f"./county_models/{user_input}/")
    # generate predictions
#    future_pred_count = 1
#    future = []
#    batch = X_test_sc[-future_pred_count:].reshape((1, future_pred_count, 1))
#    new_model.predict(batch)[0].shape

#    for i in range(22):
#        pred = new_model.predict(batch)[0]
#        future.append(pred)
#        batch = np.append(batch[:, 0:, :], [[pred[i]]] , axis = 1)

#    dates = [selected_df.index[-1] + pd.tseries.offsets.DateOffset(days = x) for x in range(0, 23)]
#    future_date = pd.DataFrame(index = dates[1:], columns = X.columns)

#    df_predict = pd.DataFrame(future[21], index = future_date[-22:].index, columns = ['Prediction'])

    return render_template('results.html')

@app.route('/vaccine_distribution_table')
def vaccine_distribution_table():
    return render_template('vaccine_distribution_table.html')

@app.route('/conclusions')
def conclusions():
    return render_template('conclusions.html')

@app.route('/further_steps')
def further_steps():
    return render_template('further_steps.html')

# route 5: accept the form submission and do something fancy with it
# load in the form data from the incoming request
# manipulate data into a format that we pass to our model
# Call app.run(debug=True) when python script is called
if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT", 8083)))
