--  sub query----- in query in another query
-- outer query for get output
-- inner query form a condition
-- TYPES
-- singele row , multi row ,multi col,nested,correlated

-- SINGLE ROW ---  condition formed has single row with single col )using (=,<,>,<=,>=,!=)
select * from employee;
select * from employee where salary>=
(select salary from employee where emp_name ='priya');

alter table employee add column city varchar (40);
UPDATE employee SET city = 'Hyderabad' WHERE emp_id = 101;
UPDATE employee SET city = 'Bangalore' WHERE emp_id = 102;
UPDATE employee SET city = 'Bangalore' WHERE emp_id = 103;
UPDATE employee SET city = 'Hyderabad' WHERE emp_id = 104;
UPDATE employee SET city = 'Mumbai' WHERE emp_id = 105;
UPDATE employee SET city = 'Mumbai' WHERE emp_id = 106;
UPDATE employee SET city = 'Delhi' WHERE emp_id = 107;

-- multirow -----  condition returns a single col and more than one row use (in,not in)
select * from employee where city in
(select city from employee where emp_id = 101 or emp_id = 104);
