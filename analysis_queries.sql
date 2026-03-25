CREATE TABLE crop_data (
    state VARCHAR(100),
    district VARCHAR(100),
    crop_year INT,
    season VARCHAR(50),
    crop VARCHAR(100),
    area_hectares FLOAT,
    production_tonnes FLOAT,
    yield_per_hectare FLOAT
);


SELECT COUNT(*) FROM crop_data;

-- Query 1 — Top 10 crops by total production
SELECT crop,
       ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production,
       ROUND(AVG(yield_per_hectare)::NUMERIC, 2) AS avg_yield
FROM crop_data
GROUP BY crop
ORDER BY total_production DESC
LIMIT 10;

-- Query 2 — Top 10 states by total production
SELECT state,
       ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production,
       ROUND(SUM(area_hectares)::NUMERIC, 2) AS total_area
FROM crop_data
GROUP BY state
ORDER BY total_production DESC
LIMIT 10;


-- Query 3 — Season-wise production
SELECT season,
       COUNT(*) AS total_records,
       ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production,
       ROUND(AVG(yield_per_hectare)::NUMERIC, 2) AS avg_yield
FROM crop_data
GROUP BY season
ORDER BY total_production DESC;

-- Query 4 — Year-wise production trend
SELECT crop_year,
       ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production,
       ROUND(SUM(SUM(production_tonnes)) OVER (ORDER BY crop_year)::NUMERIC, 2) AS running_total
FROM crop_data
GROUP BY crop_year
ORDER BY crop_year;

--Query 5 — Best yield efficiency by state
SELECT state,
       ROUND(AVG(yield_per_hectare)::NUMERIC, 2) AS avg_yield,
       ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production
FROM crop_data
GROUP BY state
ORDER BY avg_yield DESC
LIMIT 10;

-- Query 6 — Top crop per state (Window Function)
SELECT state, crop, total_production, rank
FROM (
    SELECT state, crop,
           ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production,
           RANK() OVER (PARTITION BY state ORDER BY SUM(production_tonnes) DESC) AS rank
    FROM crop_data
    GROUP BY state, crop
) ranked
WHERE rank = 1
ORDER BY total_production DESC;

-- Query 7 — Underperforming crops (high area, low yield)
SELECT crop, state,
       ROUND(AVG(area_hectares)::NUMERIC, 2) AS avg_area,
       ROUND(AVG(yield_per_hectare)::NUMERIC, 2) AS avg_yield,
       ROUND(SUM(production_tonnes)::NUMERIC, 2) AS total_production
FROM crop_data
GROUP BY crop, state
HAVING AVG(area_hectares) > 1000
AND AVG(yield_per_hectare) < 1.0
ORDER BY avg_area DESC
LIMIT 10;


SELECT * FROM crop_data;


SELECT DISTINCT season FROM crop_data;
