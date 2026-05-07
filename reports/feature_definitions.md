duration_sec - Total time between the first and last GPS ping of a trip.  
distance_km - Calculated by summing (speed * time_delta) for each segment.  
count_hard_brakes - Any deceleration event where $accel < -3 \, m/s^2.  
harsh_accel_count - Any acceleration event where $accel > 2.5 \, m/s^2.  
idling_time - Sum of all time_delta where $speed < 1 \, km/h.  
stop_count - Count of instances where speed dropped below 1 \, km/h from a moving state.  