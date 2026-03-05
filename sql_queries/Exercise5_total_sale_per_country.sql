SELECT
    orders.shipcountry country,
    sum(orderdetails.unitprice * orderdetails.quantity * (1 - orderdetails.discount)) revenue,
    sum(orderdetails.quantity) units_sold,
    count(DISTINCT orders.orderid) total_sales -- number of orders
FROM orders LEFT JOIN orderdetails
    ON orders.orderid = orderdetails.orderid
GROUP BY country
ORDER BY revenue DESC;