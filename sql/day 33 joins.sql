-- "cross & self & outer JOIN"
show DATABASES;
create DATABASE self_join;

create TABLE cus1(id int PRIMARY KEY);

use self_join;
show tables;

use 84r;

use joins;
show tables;


select * from  customers;

select * from orders;
-- with out condition  -----cross
select * from customers join orders on customers.cus_id=orders.cus_id;
-- with condition  ---inner join
SELECT orders.ord_id,order_date,customers.first_name from customers join orders on customers.cus_id =orders.cus_id where customers.first_name ='rahul';


--  self join  --doin in same table 
-- with out condition
select * from customers join customers as c;


-- natural JOIN

