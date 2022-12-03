import flask
from flask import Flask, render_template, request, url_for
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Logistic Regression Pickle
model = pickle.load(open('model/model_lg.pkl', 'rb'))
# Scaler initialization
scaler = StandardScaler()

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rainnextdayprediction', methods=['POST'])
def rainnextdayprediction():
    '''
    For rendering results on HTML GUI
    '''
    Location = int(request.form["Location"])
    Season = int(request.form["Season"])
    Rainfall = float(request.form["Rainfall"])
    WindGustSpeed = float(request.form["WindGustSpeed"])
    AverageTemp = float(request.form["Average Temp"])
    AverageHumidity = float(request.form["Average Humidity"])
    RainToday = int(request.form["RainToday"])

    data_list = [[
        Location,
        Season,
        Rainfall,
        WindGustSpeed,
        AverageTemp,
        AverageHumidity,
        RainToday
    ]]
    pred_scaller = scaler.fit_transform(data_list)
    prediction = model.predict(pred_scaller)

    output = {
        0: "Tidak Hujan",
        1: "Hujan"
    }

    return render_template('index.html', prediction_text='The Rain Next-Day Prediction is : {}'.format(output[prediction[0]]))

if __name__ == '__index__':
    app.run(debug=True)