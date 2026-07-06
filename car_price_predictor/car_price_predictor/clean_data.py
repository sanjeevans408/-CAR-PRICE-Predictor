"""
Cleans the raw quikr_car.csv scrape into a model-ready dataframe.
Run: python clean_data.py
Produces: Cleaned_Car_data.csv
"""
import pandas as pd
import numpy as np

def clean(path="quikr_car.csv"):
    car = pd.read_csv(path)

    # 1. year: keep only rows where year is a clean 4-digit number
    car = car[car['year'].str.isnumeric()]
    car['year'] = car['year'].astype(int)

    # 2. Price: drop "Ask For Price" rows, strip commas, cast to int
    car = car[car['Price'] != 'Ask For Price']
    car['Price'] = car['Price'].str.replace(',', '').astype(int)

    # 3. kms_driven: strip " kms" and commas, drop rows where it's not numeric
    #    (a few rows have "Petrol" stuck in this column due to scraping errors)
    car['kms_driven'] = car['kms_driven'].str.split(' ').str.get(0).str.replace(',', '')
    car = car[car['kms_driven'].str.isnumeric()]
    car['kms_driven'] = car['kms_driven'].astype(int)

    # 4. fuel_type: drop missing
    car = car[~car['fuel_type'].isna()]

    # 5. name: keep first 3 words only (brand + model + variant), drop noisy long titles
    car['name'] = car['name'].str.split(' ').str.slice(0, 3).str.join(' ')

    # 6. reset index after all the filtering
    car = car.reset_index(drop=True)

    # 7. drop a known extreme outlier (>= 60 lakh) that skews the model
    car = car[car['Price'] < 6000000]

    return car


if __name__ == "__main__":
    df = clean()
    print(f"Cleaned dataset shape: {df.shape}")
    print(df.head())
    df.to_csv("Cleaned_Car_data.csv", index=False)
    print("Saved -> Cleaned_Car_data.csv")
