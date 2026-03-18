import pandas as pd

def transform(df):

    df1 = df.dropna()
    print(df1.head())

    print("Missing values removed")

    df1["timestamp"] = pd.to_datetime(df["timestamp"])
    print(df1.head())
    print("Timestamp converted to datetime")


    df1["engine_tem_f"] = df["engine_temp"] * 9/5 + 32
    print(df1.head())
    print("Engine temperature converted to Fahrenheit")

    print("Data Transformed")

    print(df1.head())

    return df1
