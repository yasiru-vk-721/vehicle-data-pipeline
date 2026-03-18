CREATE TABLE dim_vehicle (
vehicle_id TEXT PRIMARY KEY,
model TEXT,
manufacturer TEXT,
year INT
);

CREATE TABLE dim_time (
time_id SERIAL PRIMARY KEY,
timestamp TIMESTAMP
);

CREATE TABLE fact_vehicle_sensor (
vehicle_id TEXT,
engine_temp FLOAT,
rpm INT,
fuel_pressure FLOAT,
speed INT,
timestamp TIMESTAMP
);