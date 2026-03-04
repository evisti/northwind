-- 1 List all products sorted by UnitPrice, descending
SELECT productname, unitprice FROM products
ORDER BY unitprice DESC;

-- 2 Find all customers from UK and Spain
SELECT * FROM customers
WHERE country = 'Spain' OR country = 'UK';

-- 3 Find all products with more than 100 units in stock and unit price at least 25
SELECT * FROM products
where unitsinstock > 100 AND unitprice >= 25;

-- 4 All unique countries to which an order has been shipped
SELECT DISTINCT(shipcountry) FROM orders;

-- 5 All orders with order date in Oct 1996
SELECT * FROM orders
WHERE date_trunc('month', orderdate) = DATE '1996-10-01';

-- 6 Find all orders for Germany from 1996 made by EmployeeID 1, and where Freight is at least 100 and ShipRegion is null
SELECT * FROM orders
WHERE shipcountry = 'Germany'
AND date_trunc('year', orderdate) = DATE '1996-01-01'
AND employeeid = 1
AND freight >= 100
AND shipregion ISNULL;

-- 7 Find all late orders (ShippedDate larger than RequiredDate)
SELECT * FROM orders
WHERE shippeddate > requireddate;

-- 8 Find all orders with order date 1997 in Jan, Feb, Mar, and Apr from Canada
SELECT * FROM orders
WHERE date_trunc('month', orderdate) BETWEEN DATE '1997-01-01' AND DATE '1997-04-01'
AND shipcountry = 'Canada';

-- 9 Find all orders where EmployeeID is 2, 5 or 8, and ShipRegion has a value, and ShipVia is either 1 or 3. Sort ascending first on EmployeeID and then on ShipVia.
SELECT * FROM orders
WHERE employeeid IN (2, 5, 8)
AND shipregion IS NOT NULL
AND shipvia IN (1, 3)
ORDER BY employeeid, shipvia;

-- 10 Find employees who are born in 1960 or later, and where region is null
SELECT * FROM employees
WHERE birthdate >= DATE '1960-01-01'
AND region ISNULL;
