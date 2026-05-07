import pandas as pd
import numpy as np

def aggregate_trip(df_trip):
    """
    df_trip is telemetry for one trip/vehicle.
    Returns aggregated features usable by ML.
    """
    df_trip = df_trip.sort_values('eventDateTime')
    df_trip['eventDateTime'] = pd.to_datetime(df_trip['eventDateTime'])
    
    df_trip['time_delta'] = df_trip['eventDateTime'].diff().dt.total_seconds().fillna(0)
    
    duration_s = (df_trip['eventDateTime'].max() - df_trip['eventDateTime'].min()).total_seconds()
    trip_distance_km = (df_trip['speed'] * (df_trip['time_delta'] / 3600)).sum()
    
    avg_speed = df_trip['speed'].mean()
    max_speed = df_trip['speed'].max()
    speed_std = df_trip['speed'].std()
    
    speed_mps = df_trip['speed'] / 3.6
    accel = speed_mps.diff() / df_trip['time_delta'].replace(0, np.nan)
    accel = accel.fillna(0).replace([np.inf, -np.inf], 0)
    
    count_hard_brakes = (accel < -3).sum()
    harsh_accel_count = (accel > 2.5).sum()
    idling_time = df_trip[df_trip['speed'] < 1]['time_delta'].sum()
    stop_count = ((df_trip['speed'] < 1) & (df_trip['speed'].shift(1) >= 1)).sum()
    
    start_time = df_trip['eventDateTime'].min()
    
    return pd.Series({
        "duration_sec": duration_s,
        "distance_km": trip_distance_km,
        "avg_speed": avg_speed,
        "max_speed": max_speed,
        "speed_std": speed_std,
        "mean_accel": accel.mean(),
        "max_accel": accel.max(),
        "accel_std": accel.std(),
        "count_hard_brakes": count_hard_brakes,
        "harsh_accel_count": harsh_accel_count,
        "idling_time": idling_time,
        "stop_count": stop_count,
        "day_of_week": start_time.dayofweek,
        "hour_of_day": start_time.hour
    })