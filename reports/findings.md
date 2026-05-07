Top Features Driving Predictions

Based on the SHAP analysis, the safety score is influenced by:
    Count of Hard Brakes is the most significant factor. High values correlate strongly with higher (riskier) safety scores.

    Harsh Acceleration Count is the second most influential feature.

    Max Speed is third that shows minimal impact compared to braking and acceleration.
    
Error Analysis & Model Quality
    The Predicted vs. Actual plot shows a near-perfect linear relationship, indicating the Random Forest model has successfully mapped the underlying heuristic formula.

    The maximum absolute error observed was approximately 3.26 units. These small discrepancies likely from the model's approximation of the linear weights (3.0, 2.0, 0.1).

    Some trips show extremely high acceleration values in scientific notation, which suggest potential telemetry sensor errors or the need for data clipping in the preprocessing stage.
    