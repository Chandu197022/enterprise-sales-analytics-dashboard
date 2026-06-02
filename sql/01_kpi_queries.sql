-- Total Revenue
SELECT ROUND(SUM(Sales),2) AS Total_Revenue
FROM superstore;

-- Total Profit
SELECT ROUND(SUM(Profit),2) AS Total_Profit
FROM superstore;

-- Total Orders
SELECT COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM superstore;

-- Total Customers
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM superstore;

-- Profit Margin
SELECT
ROUND((SUM(Profit)/SUM(Sales))*100,2)
AS Profit_Margin
FROM superstore;