from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('backend\model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([data['GrLivArea'], data['YearBuilt']]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
