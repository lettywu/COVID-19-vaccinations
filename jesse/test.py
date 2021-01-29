# imports
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from flask import Flask, request, Response, render_template, jsonify


counties_df = pd.read_csv('../clean_data/counties_models.csv')
counties_df['date'] = pd.to_datetime(counties_df['date'])
counties_df.set_index(['county', 'date'], inplace = True)
selected_df = counties_df.loc['Alameda']
features = ['hospitalized_covid_patients']
X = selected_df[features]
y = selected_df[['7dayrollingavg_newlyconfirmed']].values
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = False, test_size = 0.15)
# scale our data

mms = MinMaxScaler()
X_train_sc = mms.fit_transform(X_train)
X_test_sc = mms.transform(X_test)
new_model = load_model("./county_models/Alameda/")
# generate predictions
future_pred_count = 1
future = []
batch = X_test_sc[-future_pred_count:].reshape((1, future_pred_count, 1))
new_model.predict(batch)[0].shape
for i in range(22):
    pred = new_model.predict(batch)[0]
    future.append(pred)
    batch = np.append(batch[:, 0:, :], [[pred[i]]] , axis = 1)

dates = [selected_df.index[-1] + pd.tseries.offsets.DateOffset(days = x) for x in range(0, 23)]
future_date = pd.DataFrame(index = dates[1:], columns = X.columns)
df_predict = pd.DataFrame(future[21], index = future_date[-22:].index, columns = ['Prediction'])
