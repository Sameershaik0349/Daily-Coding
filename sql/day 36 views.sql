-- "views" ------  create a sub table for main table --- it is called has virtual table
-- benfits ----with this we can access easily
-- provide SECURITY to data
-- save the time 
show databases;
use sub_quries;
show tables;
select * from emp ;
-- when in comapany to print a sepcfic department 

select * from emp where department ='hr';

-- creating a view table

create view it AS 
select * from emp where department ='it';   ----- the result store in view like virtual name that we given ex--it
select * from it;

create view hr AS
select * from emp where department = 'hr';
select * from hr;

create view salary1 AS
select * from emp where salary > '70000';
SELECT * from salary1;

insert into emp values(31,"sameer","hr",99000,21,"bengulore") ; ---- after updating in main table then its also updated automatically in view TABLE  
update emp set department ='it' where name ='sameer';


--  if we  update in view table then it changes in main table also in new version like 8.044 but before 8.0.42 there is no this type method is there
 insert into salary1 values(32,"shaik","it",78000,21,"chennei");   ----this is updated in main table also


-- if we insert in view table with a wrong record then it will check first in main table then it check condtion view then it show matched view table


-- too remove view

drop view salary;


-- tooo see all view tables if we forget

use information_schema;  -------all are store in in this information_schemaa

show tables;

select * from views where table_schema ='sub_quries'     -----too see view tables in SPECIFIC dstatbase