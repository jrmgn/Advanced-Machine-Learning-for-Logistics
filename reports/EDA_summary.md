Summary of Findings:
The dataset is clean regarding structural integrity, with zero missing values across all columns (vehicleId, speed, eventDateTime) and no duplicate rows. To ensure consistency for the time-series nature of the data, the records were sorted by vehicleId and eventDateTime. A new feature, is_stationary, was created to isolate instances where the vehicle speed was exactly zero, facilitating the identification of idling states.

The average vehicle speed across the dataset is approximately 9.38 units, while the maximum recorded speed reached 71.29 units.  
Harsh driving events are rare but present. The mean for Harsh Acceleration is 1.51, while Harsh Braking is lower at 0.003.  
There is variance in driver behavior, with some vehicles recording up to 68 overspeeding events, whereas the 75th percentile of the fleet shows zero overspeeding.  
The data represents 1,350 unique vehicle summaries, with an average of 55 records per vehicle.