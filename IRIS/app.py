from flask import Flask, redirect, url_for, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__,template_folder='templates')

# Load the pickled model once when the application starts
model = pickle.load(open('model/irisclassii.pickle', 'rb'))

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sepal_length = float(request.json['sepal-length'])
        sepal_width = float(request.json['sepal-width'])
        petal_length = float(request.json['petal-length'])
        petal_width = float(request.json['petal-width'])

        # Validate input values
        if not (0 <= sepal_length <= 10 and 0 <= sepal_width <= 10 and
                0 <= petal_length <= 10 and 0 <= petal_width <= 10):
            return jsonify({'error': 'Invalid input values'}), 400

        # Make a prediction using the model
        prediction = model.predict(np.array([[sepal_length, sepal_width, petal_length, petal_width]]))[0]
        
        if prediction == 0:
            return jsonify({'url': url_for('show_setosa', _external=True)})
        elif prediction == 1:
            return jsonify({'url': url_for('show_versicolor', _external=True)})
        else:
            return jsonify({'url': url_for('show_virginica', _external=True)})
    except Exception as e:
        return jsonify({'error': 'Error occurred during prediction'}), 500

@app.route('/setosa/')
def show_setosa():
    return render_template('setosa.html')

@app.route('/versicolor/')
def show_versicolor():
    return render_template('versicolor.html')

@app.route('/virginica/')
def show_virginica():
    return render_template('virginica.html')

if __name__ == '__main__':
    app.run(debug=True)