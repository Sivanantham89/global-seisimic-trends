import pandas as pd
from sqlalchemy import create_engine


# ==============================
# MySQL connection details
# ==============================

username = "root"
password = "siva322005"
host = "localhost"
database = "seismic_db"


# Create database connection
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)


# ==============================
# Read cleaned CSV
# ==============================

file_path = "data/cleaned_earthquakes.csv"

print("Reading cleaned dataset...")

df = pd.read_csv(file_path)

print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==============================
# Convert datetime columns
# ==============================

df["time"] = pd.to_datetime(df["time"], errors="coerce")
df["updated"] = pd.to_datetime(df["updated"], errors="coerce")


# ==============================
# Upload in batches
# ==============================

print("\nUploading data to MySQL...")

chunk_size = 10000

for start in range(0, len(df), chunk_size):

    end = min(start + chunk_size, len(df))

    chunk = df.iloc[start:end]

    chunk.to_sql(
        "earthquakes",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print(f"Uploaded {end:,} / {len(df):,} rows")


print("\nUpload completed successfully!")