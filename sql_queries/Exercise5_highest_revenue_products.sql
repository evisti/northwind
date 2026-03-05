-- Highest revenue products
SELECT
    products.productname,
    sum(orderdetails.unitprice * orderdetails.quantity * (1 - orderdetails.discount)) revenue,
    sum(orderdetails.quantity) units_sold,
    avg(orderdetails.unitprice) avg_unit_price
FROM orderdetails LEFT JOIN products
    ON orderdetails.productid = products.productid
GROUP BY productname
ORDER BY revenue DESC;
