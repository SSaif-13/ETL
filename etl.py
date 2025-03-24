import os
import requests
import pandas as pd
from io import StringIO

#extracting data
def extract() -> pd.DataFrame:
    print("Extracting...")
    API_URL = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv?v=1&csvType=full&useColumnShortNames=true"
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the data, status code: {response.status_code}")
    
    data = pd.read_csv(StringIO(response.text))
    print(f"Extracted {len(data)} rows and {len(data.columns)} columns")
    return data

#transforming data
def transform(data:pd.DataFrame) -> pd.DataFrame:
    print("Transforming...")

    print("Available columns:", data.columns)
    df = data[data["Entity"]== "Canada"]
    print(f"Total Number of Canadian Entries {len(df)}")
    df = df.dropna()
    return df

#loading data
def load(df: pd.DataFrame, filename = "Canada_CO2_Data.csv"):
    print("Loading data...")
    df.to_csv(filename, index=False)
    file_path = os.path.abspath(filename) 
    print(f"Data saved to: {file_path} ")

#execution block
if __name__ == "__main__":
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)