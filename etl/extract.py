import pandas as pd

def extract():

    df = pd.read_csv("../data/sensor_data.csv")

    print(df.head())

    print("Data Extracted")
    
    return df

if __name__ == "__main__":
    extract()
