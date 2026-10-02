CREATE DATABASE seismic_db;
USE seismic_db;
SELECT DATABASE();
USE seismic_db;

CREATE TABLE earthquakes (
    id VARCHAR(50) PRIMARY KEY,
    time DATETIME,
    updated DATETIME,
    latitude DOUBLE,
    longitude DOUBLE,
    depth_km DOUBLE,
    mag DOUBLE,
    magType VARCHAR(20),
    place TEXT,
    status VARCHAR(30),
    tsunami INT,
    sig INT,
    net VARCHAR(20),
    nst DOUBLE,
    dmin DOUBLE,
    rms DOUBLE,
    gap DOUBLE,
    magError DOUBLE,
    depthError DOUBLE,
    magNst DOUBLE,
    locationSource VARCHAR(50),
    magSource VARCHAR(50),
    types TEXT,
    ids TEXT,
    sources TEXT,
    type VARCHAR(50),

    year INT,
    month INT,
    day INT,
    day_of_week VARCHAR(20),
    depth_category VARCHAR(20),
    magnitude_category VARCHAR(20),
    location_region VARCHAR(100)
);
DESCRIBE earthquakes;
SELECT COUNT(*) FROM earthquakes;
USE seismic_db;

SELECT COUNT(*) AS total_records
FROM earthquakes;

SELECT *
FROM earthquakes
LIMIT 5;

USE seismic_db;

SELECT
    id,
    time,
    place,
    mag,
    depth_km,
    latitude,
    longitude
FROM earthquakes
WHERE type = 'earthquake'
ORDER BY mag DESC
LIMIT 10;

USE seismic_db;

SELECT
    id,
    time,
    place,
    mag,
    depth_km,
    latitude,
    longitude
FROM earthquakes
WHERE type = 'earthquake'
ORDER BY depth_km DESC
LIMIT 10;

SELECT id, time, place, mag, depth_km, latitude, longitude
FROM earthquakes
WHERE type = 'earthquake'
ORDER BY depth_km DESC
LIMIT 10;

SELECT id, time, place, mag, depth_km, latitude, longitude
FROM earthquakes
WHERE type = 'earthquake'
  AND depth_km < 50
  AND mag > 7.5
ORDER BY mag DESC;


SELECT
    magType,
    ROUND(AVG(mag), 2) AS average_magnitude,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY magType
ORDER BY average_magnitude DESC;

SELECT
    year,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY year
ORDER BY year;

SELECT
    month,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY month
ORDER BY month;

SELECT
    day_of_week,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY day_of_week
ORDER BY earthquake_count DESC;

SELECT
    net,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY net
ORDER BY earthquake_count DESC; 

SELECT
    status,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY status
ORDER BY earthquake_count DESC;

SELECT
    type,
    COUNT(*) AS event_count
FROM earthquakes
GROUP BY type
ORDER BY event_count DESC;

SELECT
    ROUND(AVG(rms), 2) AS average_rms,
    ROUND(AVG(gap), 2) AS average_gap
FROM earthquakes
WHERE type = 'earthquake';

SELECT
    id,
    place,
    mag,
    nst
FROM earthquakes
WHERE type = 'earthquake'
  AND nst >= 100
ORDER BY nst DESC;

SELECT
    year,
    COUNT(*) AS tsunami_earthquakes
FROM earthquakes
WHERE type = 'earthquake'
  AND tsunami = 1
GROUP BY year
ORDER BY year;

SELECT
    tsunami,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY tsunami;

SELECT
    magnitude_category,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY magnitude_category;

SELECT
    year,
    ROUND(AVG(mag), 2) AS average_magnitude
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY year
ORDER BY year;

SELECT
    year,
    ROUND(AVG(depth_km), 2) AS average_depth_km
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY year
ORDER BY year;

SELECT
    location_region,
    ROUND(AVG(mag), 2) AS average_magnitude,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
  AND location_region IS NOT NULL
GROUP BY location_region
HAVING COUNT(*) >= 10
ORDER BY average_magnitude DESC
LIMIT 5;

SELECT
    location_region,
    SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) AS shallow_count,
    SUM(CASE WHEN depth_km >= 50 THEN 1 ELSE 0 END) AS deep_count
FROM earthquakes
WHERE type = 'earthquake'
  AND location_region IS NOT NULL
GROUP BY location_region
HAVING shallow_count > 0
   AND deep_count > 0
ORDER BY location_region;



SELECT
    location_region,
    COUNT(*) AS earthquake_count,
    ROUND(AVG(mag), 2) AS average_magnitude
FROM earthquakes
WHERE type = 'earthquake'
  AND location_region IS NOT NULL
GROUP BY location_region
HAVING COUNT(*) >= 50
ORDER BY earthquake_count DESC, average_magnitude DESC
LIMIT 3;

SELECT
    ROUND(AVG(depth_km), 2) AS average_depth_km,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
  AND latitude BETWEEN -10 AND 10;
  
  SELECT
    location_region,
    SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) AS shallow_count,
    SUM(CASE WHEN depth_km >= 50 THEN 1 ELSE 0 END) AS deep_count,
    ROUND(
        SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) /
        NULLIF(SUM(CASE WHEN depth_km >= 50 THEN 1 ELSE 0 END), 0),
        2
    ) AS shallow_deep_ratio
FROM earthquakes
WHERE type = 'earthquake'
  AND location_region IS NOT NULL
GROUP BY location_region
HAVING deep_count > 0
ORDER BY shallow_deep_ratio DESC
LIMIT 1;

SELECT
    tsunami,
    ROUND(AVG(mag), 2) AS average_magnitude,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE type = 'earthquake'
GROUP BY tsunami;

SELECT
    id,
    place,
    mag,
    gap,
    rms
FROM earthquakes
WHERE type = 'earthquake'
  AND (gap > 180 OR rms > 1)
ORDER BY gap DESC, rms DESC;

SELECT
    location_region,
    COUNT(*) AS deep_focus_count,
    ROUND(AVG(mag), 2) AS average_magnitude
FROM earthquakes
WHERE type = 'earthquake'
  AND depth_km > 300
  AND location_region IS NOT NULL
GROUP BY location_region
ORDER BY deep_focus_count DESC;