import requests
import pandas as pd
from datetime import datetime
import time


# USGS API
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"


# -----------------------------------
# Settings
# -----------------------------------

start_year = 2021
start_month = 1

end_year = 2025
end_month = 12


# Store all earthquake records
all_records = []


# -----------------------------------
# Download data month by month
# -----------------------------------

for year in range(start_year, end_year + 1):

    for month in range(1, 13):

        # Skip months before our starting month
        if year == start_year and month < start_month:
            continue

        # Stop after our ending month
        if year == end_year and month > end_month:
            break

        # Create start date
        start_date = f"{year}-{month:02d}-01"

        # Calculate next month
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1

        end_date = f"{next_year}-{next_month:02d}-01"

        print(f"Downloading: {start_date} to {end_date}")

        params = {
            "starttime": start_date,
            "endtime": end_date,
            "format": "geojson"
        }

        try:

            response = requests.get(url, params=params)

            print("Status:", response.status_code)

            response.raise_for_status()

            data = response.json()

            earthquakes = data["features"]

            print("Earthquakes found:", len(earthquakes))

            # Extract each earthquake
            for earthquake in earthquakes:

                properties = earthquake["properties"]
                geometry = earthquake["geometry"]

                coordinates = geometry.get("coordinates", [None, None, None])

                record = {
                    "id": earthquake.get("id"),

                    "time": properties.get("time"),
                    "updated": properties.get("updated"),

                    "latitude": coordinates[1],
                    "longitude": coordinates[0],
                    "depth_km": coordinates[2],

                    "mag": properties.get("mag"),
                    "magType": properties.get("magType"),
                    "place": properties.get("place"),
                    "status": properties.get("status"),
                    "tsunami": properties.get("tsunami"),
                    "sig": properties.get("sig"),
                    "net": properties.get("net"),
                    "nst": properties.get("nst"),
                    "dmin": properties.get("dmin"),
                    "rms": properties.get("rms"),
                    "gap": properties.get("gap"),
                    "magError": properties.get("magError"),
                    "depthError": properties.get("depthError"),
                    "magNst": properties.get("magNst"),
                    "locationSource": properties.get("locationSource"),
                    "magSource": properties.get("magSource"),
                    "types": properties.get("types"),
                    "ids": properties.get("ids"),
                    "sources": properties.get("sources"),
                    "type": properties.get("type")
                }

                all_records.append(record)

            # Small delay between requests
            time.sleep(0.2)

        except Exception as e:

            print("Error:", e)


# -----------------------------------
# Create DataFrame
# -----------------------------------

df = pd.DataFrame(all_records)


# Remove duplicate earthquake IDs
df = df.drop_duplicates(subset="id")


# -----------------------------------
# Display information
# -----------------------------------

print("\n==============================")
print("DATA COLLECTION COMPLETED")
print("==============================")

print("Total earthquakes:", len(df))

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# -----------------------------------
# Save raw dataset
# -----------------------------------

df.to_csv("data/raw_earthquakes.csv", index=False)

print("\nDataset saved successfully!")