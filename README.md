Driver Performance & Safety Scoring System 

This project processes vehicle telemetry data to predict a "Safety Score" based on driving behavior.

Project Structure
- data: Raw telemetry and processed trip features.
- notebooks: EDA, Feature Engineering, Training, Explainability (SHAP), and Demo.
- src: Python scripts for data preparation, training, and the Flask API.
- models: Saved `safety_model.pkl` artifact.

Quick Start
1. Install Dependencies
pip install -r requirements.txt

2. Run the Training Pipeline
To retrain the model with the latest features:
cd src
python train.py

3. Start the API Service
To start the real-time prediction server:
cd src
python serve.py

4. Test a Prediction
Use curl in your terminal to get a score:
curl -X POST [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict) -H "Con

Key Findings
Primary Risk Factor: Hard Braking behavior has the highest impact on the safety score.
Model Performance: Achieved a high R2 Score and low MAE, indicating stable predictions across different trip types.
Explainability: Used SHAP to visualize how individual features push a driver's score toward high or low risk.
