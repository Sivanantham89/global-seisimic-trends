# Global Seismic Trends: Data-Driven Earthquake Insights

## 1. Project Title

Global Seismic Trends: Data-Driven Earthquake Insights

---

## 2. Problem Statement

The project focuses on analyzing global earthquake data to identify
seismic patterns, trends, and risk-related insights using data-driven
techniques.

The system collects earthquake data, performs data preprocessing,
stores the cleaned data in a MySQL database, performs SQL analysis,
and presents the results through a Streamlit dashboard.

---

## 3. Objectives

- Collect global earthquake data using the USGS Earthquake API.
- Clean and preprocess the collected earthquake dataset.
- Handle missing and duplicate values.
- Convert timestamp information into useful date-related features.
- Store the cleaned dataset in MySQL.
- Perform SQL-based earthquake analysis.
- Perform Python-based data analysis and visualization.
- Develop an interactive Streamlit dashboard.
- Identify earthquake patterns based on magnitude, depth, time,
  tsunami activity, and other available features.

---

## 4. Technologies Used

- Python
- Pandas
- Requests
- Regular Expressions
- Matplotlib
- MySQL
- SQLAlchemy
- PyMySQL
- Streamlit
- MySQL Workbench

---

## 5. Data Collection

Earthquake data was collected from the USGS Earthquake API.

API endpoint:

https://earthquake.usgs.gov/fdsnws/event/1/query

The data was collected month-by-month for the project time period
and stored as a CSV dataset.

The collected dataset contains 26 original USGS features.

---

## 6. Data Preprocessing

The collected earthquake data was cleaned using Python and Pandas.

The preprocessing included:

- Converting timestamp fields into datetime format.
- Converting numeric fields into appropriate numeric data types.
- Handling missing numeric values.
- Removing duplicate earthquake IDs.
- Extracting year, month, day, and day of week.
- Creating depth categories.
- Creating magnitude categories.
- Cleaning and extracting location information from the place field.

The cleaned dataset contains 762,106 records and 33 columns.

---

## 7. MySQL Database

A MySQL database named `seismic_db` was created.

The cleaned earthquake data was stored in the:

`earthquakes`

table.

The data was uploaded from Python using SQLAlchemy and PyMySQL.

---

## 8. SQL Analysis

SQL queries were used to analyze:

- Strongest earthquakes.
- Deepest earthquakes.
- Shallow high-magnitude earthquakes.
- Magnitude types.
- Yearly earthquake trends.
- Monthly earthquake trends.
- Day-of-week trends.
- Reporting networks.
- Earthquake status.
- Tsunami activity.
- Earthquake depth.
- Earthquake magnitude.
- Earthquake reliability indicators.
- Deep-focus earthquakes.
- Other required project-level analytical tasks.

---

## 9. Python Analysis

Python and Pandas were used for additional analysis and visualization.

Matplotlib was used to create charts for:

- Earthquake count by year.
- Earthquake count by month.
- Magnitude distribution.
- Depth distribution.
- Tsunami distribution.
- Shallow versus deep earthquakes.
- Day-of-week distribution.

---

## 10. Streamlit Dashboard

A Streamlit dashboard was developed to provide an interactive view
of the earthquake dataset.

The dashboard provides:

- Key earthquake statistics.
- Minimum magnitude filtering.
- Year filtering.
- Depth-category filtering.
- Yearly earthquake trends.
- Monthly earthquake trends.
- Magnitude distribution.
- Depth distribution.
- Tsunami analysis.
- Shallow versus deep earthquake analysis.
- Earthquake data table.
- Global earthquake visualization.

---

## 11. Results

The project successfully processed a large global earthquake dataset
and transformed the raw API data into a cleaned analytical dataset.

The analysis provides insights into:

- Earthquake magnitude patterns.
- Earthquake depth patterns.
- Yearly and monthly earthquake activity.
- Tsunami-related earthquake activity.
- Distribution of shallow and deep earthquakes.
- Earthquake measurement and reliability information.

The Streamlit dashboard provides an interactive interface for
exploring these results.

---

## 12. Conclusion

The project demonstrates a complete data analytics workflow for
global earthquake data.

The workflow includes API-based data collection, preprocessing,
MySQL storage, SQL analysis, Python visualization, and Streamlit
dashboard development.

The resulting system provides a data-driven approach for exploring
global seismic trends and earthquake characteristics.