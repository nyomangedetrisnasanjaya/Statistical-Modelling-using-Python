from flask import Flask, render_template, request
import numpy as np
from logging import debug
import pickle

# Model
model = pickle.load(open('model/model_RF.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heartfailureprediction', methods=['POST'])
def heartfailureprediction():
    '''
    For rendering results on HTML GUI
    '''
    usia = float(request.form["usia"])
    anaemia = float(request.form["anaemia"])
    creatinin_fosfokinase = float(request.form["creatinin_fosfokinase"])
    fraksi_ejeksi = float(request.form["fraksi_ejeksi"])
    tekanan_darah_tinggi = float(request.form["tekanan_darah_tinggi"])
    platelets = float(request.form["platelets"])
    kreatinin_serum = float(request.form["kreatinin_serum"])
    sodium_serum = float(request.form["sodium_serum"])
    time = float(request.form["time"])

    data_list = [[
        usia,
        anaemia,
        creatinin_fosfokinase,
        fraksi_ejeksi,
        tekanan_darah_tinggi,
        platelets,
        kreatinin_serum,
        sodium_serum,
        time
    ]]
    prediction = model.predict(data_list)

    output = {
        0: "Tidak Meninggal",
        1: "Meninggal"
    }

    return render_template('index.html', prediction_text='The Survival of Patients Prediction is : {}'.format(output[prediction[0]]))

if __name__ == '__index__':
    app.run(debug=True)