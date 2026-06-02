-- Top Cities by Sales

SELECT
City,
ROUND(SUM(Sales),2)
AS Revenue
FROM superstore
GROUP BY City
ORDER BY Revenue DESC
LIMIT 10;

-- Sales by Region

SELECT
Region,
ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY Region
ORDER BY Revenue DESC;

-- Sales by State

SELECT
State,
ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY State
ORDER BY Revenue DESC;