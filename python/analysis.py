import pandas as pd
import matplotlib.pyplot as plt

# ========================================================
# LOAD DATA
# ========================================================

df = pd.read_csv("data/cleaned_earthquakes.csv")

df["time"] = pd.to_datetime(df["time"])

# Keep actual earthquakes
earthquakes = df[df["type"] == "earthquake"].copy()

print("Total earthquake records:", len(earthquakes))


# ========================================================
# 1. EARTHQUAKE COUNT BY YEAR
# ========================================================

yearly_count = earthquakes.groupby("year").size()

print("\nEarthquake Count by Year:")
print(yearly_count)

plt.figure(figsize=(8, 5))
yearly_count.plot(kind="bar")

plt.title("Earthquake Count by Year")
plt.xlabel("Year")
plt.ylabel("Number of Earthquakes")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("output/earthquakes_by_year.png")
plt.close()


# ========================================================
# 2. EARTHQUAKE COUNT BY MONTH
# ========================================================

monthly_count = earthquakes.groupby("month").size()

print("\nEarthquake Count by Month:")
print(monthly_count)

plt.figure(figsize=(8, 5))
monthly_count.plot(kind="line", marker="o")

plt.title("Earthquake Count by Month")
plt.xlabel("Month")
plt.ylabel("Number of Earthquakes")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()

plt.savefig("output/earthquakes_by_month.png")
plt.close()


# ========================================================
# 3. MAGNITUDE DISTRIBUTION
# ========================================================

plt.figure(figsize=(8, 5))

earthquakes["mag"].plot(
    kind="hist",
    bins=30
)

plt.title("Earthquake Magnitude Distribution")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("output/magnitude_distribution.png")
plt.close()


# ========================================================
# 4. DEPTH DISTRIBUTION
# ========================================================

plt.figure(figsize=(8, 5))

earthquakes["depth_km"].plot(
    kind="hist",
    bins=30
)

plt.title("Earthquake Depth Distribution")
plt.xlabel("Depth (km)")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("output/depth_distribution.png")
plt.close()


# ========================================================
# 5. TSUNAMI VS NON-TSUNAMI
# ========================================================

tsunami_count = earthquakes["tsunami"].value_counts()

print("\nTsunami Distribution:")
print(tsunami_count)

labels = ["Non-Tsunami", "Tsunami"]

plt.figure(figsize=(7, 5))

tsunami_count.plot(
    kind="bar"
)

plt.title("Tsunami vs Non-Tsunami Earthquakes")
plt.xlabel("Tsunami Status (0 = No, 1 = Yes)")
plt.ylabel("Number of Earthquakes")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("output/tsunami_distribution.png")
plt.close()


# ========================================================
# 6. SHALLOW VS DEEP
# ========================================================

depth_count = earthquakes["depth_category"].value_counts()

print("\nDepth Category:")
print(depth_count)

plt.figure(figsize=(7, 5))

depth_count.plot(
    kind="bar"
)

plt.title("Shallow vs Deep Earthquakes")
plt.xlabel("Depth Category")
plt.ylabel("Number of Earthquakes")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("output/depth_category.png")
plt.close()


# ========================================================
# 7. EARTHQUAKES BY DAY OF WEEK
# ========================================================

day_count = earthquakes["day_of_week"].value_counts()

print("\nEarthquakes by Day of Week:")
print(day_count)

plt.figure(figsize=(9, 5))

day_count.plot(
    kind="bar"
)

plt.title("Earthquakes by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Earthquakes")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output/day_of_week.png")
plt.close()


# ========================================================
# COMPLETED
# ========================================================

print("\n======================================")
print("PYTHON ANALYSIS COMPLETED SUCCESSFULLY")
print("======================================")

print("\nCharts saved in:")
print("D:\\1st_project\\output")