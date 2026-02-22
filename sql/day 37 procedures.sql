-- procedures ------ reuse the  block of commands
-- ----> save time and space complexity



-- -- delimiter $$

-- -- create procedure procedure_name()
-- begin
-- --commands
-- end$$;
--- delimiter


-- calling the procedure;
show DATABASES;

create DATABASE procedures;
use sub_quries;


DELIMITER $$
create Procedure salaar()
begin
SELECT * from emp where age >35;
end $$
DELIMITER;
call salaar();

DELIMITER $$
CREATE procedure mahendra(a int)
begin
select * from emp where age >a;
end$$
DELIMITER;
call mahendra(20)

select * from emp;

DELIMITER$$;
create procedure inserting(a int,b varchar(20),c varchar(20),d float,e int,f varchar(20))
begin
insert into emp values(a,b,c,d,e,f);
end$$
DELIMITER;
call inserting(33,"bahubali","actor",960000,50,"mahishmathi");
select * from emp;


DELIMITER$$
create procedure fun(a int,b varchar(20),c varchar(20),d float,e int,f varchar(20))
begin
insert into emp values(a,b,c,d,e,f);
end$$
DELIMITER;
call fun(34,"rana","actor",960000,50,"mahishmathi");
select * from emp;
drop procedure fun;

-----------------update
delimiter $$;
CREATE Procedure new1(a varchar(20),b varchar(20))
begin
update emp set name =a where name =b;
end $$
DELIMITER;

call new1('amit','rebel');
select * from emp;


drop PROCEDURE new;


DELIMITER $$
create Procedure sameera()
begin
select * from emp where salary > 70000;
end $$
DELIMITER;

call sameera()


drop Procedure sameera;


DELIMITER $$
create procedure sam(a int)
begin
select * from emp where age > a;
end$$
DELIMITER;

call sam(30)


DELIMITER $$
create procedure inserting1(a int,b varchar(20),c varchar(20),d FLOAT,e int,f varchar(20))
begin
insert into emp values(a,b,c,d,e,f);
end$$
delimiter;
call inserting1(35,"sameeeer",'sdDcsd',123456,2324,"DFSGVX");
call inserting1;

select * from emp;