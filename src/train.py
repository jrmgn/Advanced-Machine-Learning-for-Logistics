import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestRegressor

data_path = '../data/processed/trip_features.csv'
df = pd.read_csv(data_path)

df['safety_score'] = (df['count_hard_brakes'] * 3.0) + \
                     (df['harsh_accel_count'] * 2.0) + \
                     (df['max_speed'] * 0.1)

X = df.drop(columns=['vehicleId', 'safety_score'])
y = df['safety_score']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

os.makedirs('../models', exist_ok=True)
joblib.dump(model, '../models/baseline_model.pkl')

print("Success: Model saved to models/baseline_model.pkl")