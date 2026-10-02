import pandas as pd
import numpy as np
import re

# Load raw dataset
df = pd.read_csv("data/raw_earthquakes.csv")

print("Original shape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
df["time"] = pd.to_datetime(df["time"], unit="ms", errors="coerce")

df["updated"] = pd.to_datetime(
    df["updated"],
    unit="ms",
    errors="coerce"
)
numeric_columns = [
    "mag",
    "depth_km",
    "nst",
    "dmin",
    "rms",
    "gap",
    "magError",
    "depthError",
    "magNst",
    "sig"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    measurement_columns = [
    "mag",
    "depth_km",
    "nst",
    "dmin",
    "rms",
    "gap",
    "magError",
    "depthError",
    "magNst",
    "sig"
]

for column in measurement_columns:
    df[column] = df[column].fillna(df[column].median())
    df["tsunami"] = df["tsunami"].fillna(0)
df = df.drop_duplicates(subset="id")
print("\nShape after removing duplicates:")
print(df.shape)
df["year"] = df["time"].dt.year

df["month"] = df["time"].dt.month

df["day"] = df["time"].dt.day

df["day_of_week"] = df["time"].dt.day_name()
df["depth_category"] = np.where(
    df["depth_km"] < 50,
    "Shallow",
    "Deep"
)
df["magnitude_category"] = np.where(
    df["mag"] >= 7.5,
    "Strong",
    "Normal"
)
def extract_location(place):

    if pd.isna(place):
        return None

    match = re.search(r",\s*([^,]+)$", place)

    if match:
        return match.group(1).strip()

    return None


df["location_region"] = df["place"].apply(extract_location)
text_columns = [
    "magType",
    "status",
    "type",
    "net",
    "sources",
    "types"
]

for column in text_columns:

    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
        .str.lower()
    )
    print("\n==============================")
print("CLEANING COMPLETED")
print("==============================")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSample cleaned data:")
print(
    df[
        [
            "id",
            "time",
            "latitude",
            "longitude",
            "depth_km",
            "mag",
            "place",
            "location_region",
            "year",
            "month",
            "day_of_week",
            "depth_category",
            "magnitude_category"
        ]
    ].head()
)
df.to_csv(
    "data/cleaned_earthquakes.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
