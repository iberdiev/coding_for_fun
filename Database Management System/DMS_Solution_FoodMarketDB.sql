-- 1
SELECT *
FROM Product
WHERE UnitPrice > 7 AND
(ProductName LIKE '%Syrup%' OR
ProductName LIKE '%Teatime%')
;

-- 2
SELECT city
FROM Customer
GROUP BY city
HAVING COUNT(ID) > 1
ORDER BY city
;

-- 3
select supplierid, avg(unitprice)
from product
group by supplierid
having avg(unitprice)>10
order by supplierid;

-- 4
select customer.id, customer.firstname, orders.id as "orderID"
from orders, customer
where customer.id = orders.customerid
order by customer.firstname
;

-- 5
select customer.id, customer.firstname, orders.id as "orderID"
from orders, customer
where customer.id = orders.customerid or (customer.id = null)
order by customer.firstname
;

-- 6
select customer.id, concat(customer.firstname, ' ', customer.lastname) as "Name", city,
orders.id as "OrderID", orderitem.quantity, productname, product.unitprice,
orderitem.quantity * product.unitprice as "Total price"
from customer, orders, orderitem, product
where customer.id = orders.customerid
and orderitem.orderid = orders.id
and product.id = orderitem.productid
order by customer.id
;

-- 7
(select concat(customer.firstname, ' ', customer.lastname) as "Name"
from customer)
except
(select concat(customer.firstname, ' ', customer.lastname) as "Name"
from customer, orders, orderitem, product
where customer.id = orders.customerid
and orderitem.orderid = orders.id
and product.id = orderitem.productid
and product.productname = 'Filo Mix'
group by customer.id);

-- 8
select orders.id
from orders, orderitem, product
where orders.id = orderitem.orderid
and product.id = orderitem.productid
and product.productname = 'Chang';

-- 9
select *
from product
where unitprice = (select max(unitprice) from product);

-- 10
select productname, unitprice
from product
where unitprice > (select avg(unitprice) from product)
;

-- 11
select orders.customerid, concat(customer.firstname, ' ', customer.lastname) as "Name",
quantity
from orders, orderitem, customer
where orders.id = orderitem.orderid
and customer.id = orders.customerid
and (orderitem.quantity = (select min(quantity) from orderitem)
or orderitem.quantity = (select max(quantity) from orderitem));

-- 12
with p1 as (
select customer.id as c1
from customer, product, orders, orderitem
where customer.id = orders.CustomerID
and orders.id = orderitem.orderID
and product.id = orderitem.ProductID
and (product.id = 1)
), p2 as (
select customer.id as c2
from customer, product, orders, orderitem
where customer.id = orders.CustomerID
and orders.id = orderitem.orderID
and product.id = orderitem.ProductID
and (product.id = 3)
)
select concat(customer.firstname, ' ', customer.lastname) as "Name"
from p1, p2, customer
where c1 = c2
and c1 = customer.id
group by customer.id;

-- 13
select product.id
from product, orderitem
where product.id = orderitem.productid
group by product.id
having sum(quantity) > 5
order by product.id;

-- 14
select orders.id as "OrderID", count(orderitem.quantity) as "NumProductsOnOrder"
from orders, orderitem
where orders.id = orderitem.orderid
group by orders.id
having count(orderitem.quantity)>= 3
order by orders.id;
