from flask import Flask, render_template, request
import numpy as np
import pickle

# Model
model = pickle.load(open('model/model_km.pkl', 'rb'))
# Scaler
scaler = pickle.load(open('model/scaler_model.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/creditcardclustering', methods=['POST'])
def creditcardclustering():
    '''
    For rendering results on HTML GUI
    '''
    BALANCE = float(request.form["BALANCE"])
    BALANCE_FREQUENCY = float(request.form["BALANCE_FREQUENCY"])
    PURCHASES = float(request.form["PURCHASES"])
    ONEOFF_PURCHASES = float(request.form["ONEOFF_PURCHASES"])
    INSTALLMENTS_PURCHASES = float(request.form["INSTALLMENTS_PURCHASES"])
    CASH_ADVANCE = float(request.form["CASH_ADVANCE"])
    PURCHASES_FREQUENCY = float(request.form["PURCHASES_FREQUENCY"])
    ONEOFF_PURCHASES_FREQUENCY = float(
        request.form["ONEOFF_PURCHASES_FREQUENCY"])
    PURCHASES_INSTALLMENTS_FREQUENCY = float(
        request.form["PURCHASES_INSTALLMENTS_FREQUENCY"])
    CASH_ADVANCE_FREQUENCY = float(request.form["CASH_ADVANCE_FREQUENCY"])
    CASH_ADVANCE_TRX = float(request.form["CASH_ADVANCE_TRX"])
    PURCHASES_TRX = float(request.form["PURCHASES_TRX"])
    CREDIT_LIMIT = float(request.form["CREDIT_LIMIT"])
    PAYMENTS = float(request.form["PAYMENTS"])
    MINIMUM_PAYMENTS = float(request.form["MINIMUM_PAYMENTS"])
    PRC_FULL_PAYMENT = float(request.form["PRC_FULL_PAYMENT"])
    TENURE = float(request.form["TENURE"])

    data_list = [
        BALANCE,
        BALANCE_FREQUENCY,
        PURCHASES,
        ONEOFF_PURCHASES,
        INSTALLMENTS_PURCHASES,
        CASH_ADVANCE,
        PURCHASES_FREQUENCY,
        ONEOFF_PURCHASES_FREQUENCY,
        PURCHASES_INSTALLMENTS_FREQUENCY,
        CASH_ADVANCE_FREQUENCY,
        CASH_ADVANCE_TRX,
        PURCHASES_TRX,
        CREDIT_LIMIT,
        PAYMENTS,
        MINIMUM_PAYMENTS,
        PRC_FULL_PAYMENT,
        TENURE
    ]

    data_list = scaler.fit_transform([data_list])
    prediction = model.predict(data_list)

    return render_template('index.html', prediction_text='You belong to Cluster : {}'.format(prediction))

if __name__ == '__index__':
    app.run(debug=True)