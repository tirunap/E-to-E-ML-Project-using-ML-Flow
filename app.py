from flask import Flask, render_template, request, jsonify
import os
import numpy as np 
import pandas as pd
from pathlib import Path
from mlProject.pipeline.prediction import PredictionPipeline
from mlProject.utils.common import read_yaml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Get form data
        data = {
            'fixed acidity': float(request.form['fixed_acidity']),
            'volatile acidity': float(request.form['volatile_acidity']),
            'citric acid': float(request.form['citric_acid']),
            'residual sugar': float(request.form['residual_sugar']),
            'chlorides': float(request.form['chlorides']),
            'free sulfur dioxide': float(request.form['free_sulfur_dioxide']),
            'total sulfur dioxide': float(request.form['total_sulfur_dioxide']),
            'density': float(request.form['density']),
            'pH': float(request.form['pH']),
            'sulphates': float(request.form['sulphates']),
            'alcohol': float(request.form['alcohol'])
        }
        
        # Create DataFrame
        df = pd.DataFrame([data])
        
        # Load model and predict
        model_path = Path('artifacts/model_trainer/model.joblib')
        pipeline = PredictionPipeline(model_path)
        prediction = pipeline.predict(df)[0]
        
        return render_template('index.html', prediction=int(prediction))


@app.route('/train', methods=['GET'])
def training():
    os.system('python main.py')
    return "Training Successfulll"

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000,debug=True)