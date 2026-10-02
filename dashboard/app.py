import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Global Seismic Trends",
    page_icon="🌍",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("🌍 Global Seismic Trends")
st.subheader("Data-Driven Earthquake Insights")

st.write(
    "Interactive dashboard for analyzing global earthquake "
    "patterns, magnitude, depth and tsunami activity."
)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/cleaned_earthquakes.csv.zip",
        compression="zip"
    )

    df["time"] = pd.to_datetime(df["time"])

    return df


df = load_data()


# =====================================================
# EARTHQUAKE DATA ONLY
# =====================================================

earthquakes = df[
    df["type"] == "earthquake"
].copy()


# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🔎 Filters")

# Magnitude filter
min_mag = float(earthquakes["mag"].min())
max_mag = float(earthquakes["mag"].max())

magnitude = st.sidebar.slider(
    "Minimum Magnitude",
    min_value=min_mag,
    max_value=max_mag,
    value=0.0,
    step=0.1
)


# Year filter
years = sorted(earthquakes["year"].unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)


# Depth filter
depth_options = sorted(
    earthquakes["depth_category"].dropna().unique()
)

selected_depth = st.sidebar.multiselect(
    "Depth Category",
    depth_options,
    default=depth_options
)


# Apply filters
filtered_df = earthquakes[
    (earthquakes["mag"] >= magnitude)
    & (earthquakes["year"].isin(selected_years))
    & (earthquakes["depth_category"].isin(selected_depth))
]


# =====================================================
# KEY STATISTICS
# =====================================================

st.header("📊 Key Statistics")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Earthquakes",
        f"{len(filtered_df):,}"
    )


with col2:

    st.metric(
        "Maximum Magnitude",
        f"{filtered_df['mag'].max():.2f}"
    )


with col3:

    st.metric(
        "Average Magnitude",
        f"{filtered_df['mag'].mean():.2f}"
    )


with col4:

    st.metric(
        "Average Depth",
        f"{filtered_df['depth_km'].mean():.2f} km"
    )


# =====================================================
# YEARLY TREND
# =====================================================

st.header("📈 Earthquake Count by Year")

yearly_count = (
    filtered_df
    .groupby("year")
    .size()
)


fig, ax = plt.subplots()

yearly_count.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Year")
ax.set_ylabel("Number of Earthquakes")
ax.set_title("Earthquake Count by Year")

st.pyplot(fig)


# =====================================================
# MONTHLY TREND
# =====================================================

st.header("📅 Earthquake Count by Month")

monthly_count = (
    filtered_df
    .groupby("month")
    .size()
)


fig, ax = plt.subplots()

monthly_count.plot(
    kind="line",
    marker="o",
    ax=ax
)

ax.set_xlabel("Month")
ax.set_ylabel("Number of Earthquakes")
ax.set_title("Earthquake Count by Month")

st.pyplot(fig)


# =====================================================
# MAGNITUDE DISTRIBUTION
# =====================================================

st.header("💥 Magnitude Distribution")

fig, ax = plt.subplots()

filtered_df["mag"].plot(
    kind="hist",
    bins=30,
    ax=ax
)

ax.set_xlabel("Magnitude")
ax.set_ylabel("Frequency")
ax.set_title("Earthquake Magnitude Distribution")

st.pyplot(fig)


# =====================================================
# DEPTH DISTRIBUTION
# =====================================================

st.header("🌊 Depth Distribution")

fig, ax = plt.subplots()

filtered_df["depth_km"].plot(
    kind="hist",
    bins=30,
    ax=ax
)

ax.set_xlabel("Depth (km)")
ax.set_ylabel("Frequency")
ax.set_title("Earthquake Depth Distribution")

st.pyplot(fig)

# =====================================================
# EARTHQUAKE MAP
# =====================================================

st.header("🌍 Global Earthquake Map")

map_data = filtered_df[
    [
        "latitude",
        "longitude",
        "mag"
    ]
].dropna()

st.map(
    map_data,
    latitude="latitude",
    longitude="longitude",
    size="mag"
)


# =====================================================
# TSUNAMI ANALYSIS
# =====================================================

st.header("🌊 Tsunami Analysis")

tsunami_count = (
    filtered_df["tsunami"]
    .value_counts()
    .sort_index()
)


fig, ax = plt.subplots()

tsunami_count.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Tsunami Status")
ax.set_ylabel("Number of Earthquakes")
ax.set_title("Tsunami vs Non-Tsunami Earthquakes")

st.pyplot(fig)

# =====================================================
# TSUNAMI ANALYSIS BY YEAR
# =====================================================

st.header("🌊 Tsunami Earthquakes by Year")

tsunami_year = (
    filtered_df[
        filtered_df["tsunami"] == 1
    ]
    .groupby("year")
    .size()
)

fig, ax = plt.subplots()

tsunami_year.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Year")
ax.set_ylabel("Number of Tsunami Earthquakes")
ax.set_title("Tsunami Earthquakes by Year")

plt.xticks(rotation=0)

st.pyplot(fig)


# =====================================================
# SHALLOW VS DEEP
# =====================================================

st.header("📍 Shallow vs Deep Earthquakes")

depth_count = (
    filtered_df["depth_category"]
    .value_counts()
)


fig, ax = plt.subplots()

depth_count.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Depth Category")
ax.set_ylabel("Number of Earthquakes")
ax.set_title("Shallow vs Deep Earthquakes")

st.pyplot(fig)


# =====================================================
# DATA TABLE
# =====================================================

st.header("📋 Earthquake Data")

st.dataframe(
    filtered_df[
        [
            "id",
            "time",
            "place",
            "mag",
            "depth_km",
            "latitude",
            "longitude",
            "tsunami"
        ]
    ].head(100),
    use_container_width=True
)

# =====================================================
# TOP 10 STRONGEST EARTHQUAKES
# =====================================================

st.header("💥 Top 10 Strongest Earthquakes")

top_10 = (
    filtered_df[
        [
            "id",
            "time",
            "place",
            "mag",
            "depth_km",
            "latitude",
            "longitude"
        ]
    ]
    .sort_values("mag", ascending=False)
    .head(10)
)

st.dataframe(
    top_10,
    use_container_width=True
)

# =====================================================
# TOP 10 DEEPEST EARTHQUAKES
# =====================================================

st.header("🌊 Top 10 Deepest Earthquakes")

top_deepest = (
    filtered_df[
        [
            "id",
            "time",
            "place",
            "mag",
            "depth_km",
            "latitude",
            "longitude"
        ]
    ]
    .sort_values("depth_km", ascending=False)
    .head(10)
)

st.dataframe(
    top_deepest,
    use_container_width=True
)

# =====================================================
# SHALLOW STRONG EARTHQUAKES
# =====================================================

st.header("⚠️ Shallow Earthquakes with Magnitude > 7.5")

shallow_strong = filtered_df[
    (filtered_df["depth_km"] < 50) &
    (filtered_df["mag"] > 7.5)
].sort_values(
    "mag",
    ascending=False
)

st.dataframe(
    shallow_strong[
        [
            "id",
            "time",
            "place",
            "mag",
            "depth_km",
            "latitude",
            "longitude"
        ]
    ],
    use_container_width=True
)

st.write(
    f"Number of shallow strong earthquakes: "
    f"{len(shallow_strong):,}"
)

# =====================================================
# EARTHQUAKE STATUS
# =====================================================

st.header("📋 Earthquake Status")

status_count = (
    filtered_df["status"]
    .value_counts()
)

st.dataframe(
    status_count.reset_index().rename(
        columns={
            "status": "Status",
            "count": "Earthquake Count"
        }
    ),
    use_container_width=True
)

fig, ax = plt.subplots()

status_count.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Status")
ax.set_ylabel("Number of Earthquakes")
ax.set_title("Earthquake Status Distribution")

plt.xticks(rotation=0)

st.pyplot(fig)

# =====================================================
# EVENT TYPE ANALYSIS
# =====================================================

st.header("🔎 Earthquake Event Types")

event_type_count = (
    filtered_df["type"]
    .value_counts()
)

st.dataframe(
    event_type_count.reset_index().rename(
        columns={
            "type": "Event Type",
            "count": "Event Count"
        }
    ),
    use_container_width=True
)

fig, ax = plt.subplots()

event_type_count.head(10).plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Event Type")
ax.set_ylabel("Number of Events")
ax.set_title("Top 10 Earthquake Event Types")

plt.xticks(rotation=45)

st.pyplot(fig)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Global Seismic Trends: Data-Driven Earthquake Insights"
)