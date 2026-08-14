USE RetailDB;

SELECT * FROM customers LIMIT 5;

SELECT * FROM products LIMIT 5;

SELECT * FROM retail_sales LIMIT 5;
SELECT COUNT(*) AS Total_Customers
FROM customers;

SELECT COUNT(*) AS Total_Products
FROM products;

SELECT COUNT(*) AS Total_Sales
FROM retail_sales;
SELECT
ROUND(SUM(Sales),2) AS Total_Sales
FROM retail_sales;
SELECT
ROUND(SUM(Profit),2) AS Total_Profit
FROM retail_sales;
SELECT
ROUND(AVG(Sales),2) AS Average_Order_Value
FROM retail_sales;
SELECT
COUNT(DISTINCT Order_ID) AS Total_Orders
FROM retail_sales;
SELECT
c.Customer_Name,
ROUND(SUM(r.Sales),2) AS Total_Sales
FROM retail_sales r
JOIN customers c
ON r.Customer_ID = c.Customer_ID
GROUP BY c.Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
p.Product_Name,
ROUND(SUM(r.Sales),2) AS Total_Sales
FROM retail_sales r
JOIN products p
ON r.Product_ID = p.Product_ID
GROUP BY p.Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
p.Category,
ROUND(SUM(r.Sales),2) AS Sales
FROM retail_sales r
JOIN products p
ON r.Product_ID = p.Product_ID
GROUP BY p.Category
ORDER BY Sales DESC;
SELECT
c.Region,
ROUND(SUM(r.Sales),2) AS Sales
FROM retail_sales r
JOIN customers c
ON r.Customer_ID = c.Customer_ID
GROUP BY c.Region
ORDER BY Sales DESC;
SELECT
c.State,
ROUND(SUM(r.Sales),2) AS Sales
FROM retail_sales r
JOIN customers c
ON r.Customer_ID = c.Customer_ID
GROUP BY c.State
ORDER BY Sales DESC
LIMIT 10;
SELECT
c.Segment,
ROUND(SUM(r.Sales),2) AS Sales
FROM retail_sales r
JOIN customers c
ON r.Customer_ID = c.Customer_ID
GROUP BY c.Segment
ORDER BY Sales DESC;
SELECT
Year,
Order_Month,
ROUND(SUM(Sales),2) AS Sales
FROM retail_sales
GROUP BY Year, Order_Month
ORDER BY Year, Order_Month;