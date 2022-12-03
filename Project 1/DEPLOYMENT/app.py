import flask
from flask import Flask, render_template, request, url_for
import numpy as np
import pickle

model = pickle.load(open('model/model_reg.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ridesharingcostprediction', methods=['POST'])
def ridesharingcostprediction():
    '''
    For rendering results on HTML GUI
    '''
    features = [y for y in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('main.html', prediction_text='The Price Prediction is : $ {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)