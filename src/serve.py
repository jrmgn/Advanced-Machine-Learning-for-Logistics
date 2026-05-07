from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('../models/safety_model.pkl')

expected_features = [
    'duration_sec', 'distance_km', 'avg_speed', 'max_speed', 'speed_std', 
    'mean_accel', 'max_accel', 'accel_std', 'count_hard_brakes', 
    'harsh_accel_count', 'idling_time', 'stop_count', 'day_of_week', 'hour_of_day'
]

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return "To use this endpoint, send a POST request with JSON trip data."
        
    try:
        data = request.json
        if isinstance(data, dict):
            data = [data]
        
        X = pd.DataFrame(data)

        for col in expected_features:
            if col not in X.columns:
                X[col] = 0
        
        X = X[expected_features]
        
        prediction = model.predict(X)
        
        return jsonify({
            'status': 'success',
            'safety_scores': prediction.tolist()
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/')
def home():
    return "Driver Safety API is running! Use /predict (POST) for scores."

if __name__ == '__main__':
    app.run(debug=True, port=5000)