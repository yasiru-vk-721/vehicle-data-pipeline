from sqlalchemy import create_engine
import pandas as pd

def load(df):
    try:
        engine = create_engine("postgresql://postgres:1217321@localhost:5432/vehicle_data_etl")

        df.to_sql("vehicle_sensor_raw", engine, if_exists="append", index=False)

        print("Data Loaded into PostgreSQL")

    except Exception as e:
        print(f"Error loading data: {e}")