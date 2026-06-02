-- Category Revenue

SELECT
Category,
ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY Category
ORDER BY Revenue DESC;

-- Sub Category Revenue

SELECT
`Sub-Category`,
ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Revenue DESC;