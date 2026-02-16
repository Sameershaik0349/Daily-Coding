-- TCL-----transaaction control language
-- TRANSACTION------which will perform operations on table data
-- the operation-----{ update,insert ,delete } -----------tcl only work on this operators with only when temparary storing only

-- COMMIT---store the data permenently
-- syntax---commit;
-- ROLLBACK----recovery the data which store as temperorly
-- syntax---rollback;
-- save point ---- will store the data temperorly
-- syntax-----savepoint reference name;

show DATABASES;
create DATABASE tcl;
use tcl;
create table bank(
    id int PRIMARY KEY,
    name VARCHAR(100),
    amount decimal
);

insert into bank values (1,'rana',234567);  --- it defalut store permenently has commit;
select * from bank;
ROLLBACK;
insert into bank values (3,'prabhas',23456); 

set autocommit = 0;

set sql_safe_updates=0

DELETE from bank where id ='3';


save point 

