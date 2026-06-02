-- Top 10 Customers

SELECT
`Customer Name`,
ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY `Customer Name`
ORDER BY Revenue DESC
LIMIT 10;

-- Sales by Segment

SELECT
Segment,
ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY Segment
ORDER BY Revenue DESC;