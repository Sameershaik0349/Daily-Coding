show databases;

use 84r;

create table trigger1(
    id int,
    name varchar(20),
    bal INT
);


create table trigger2 (
    messege varchar(100),
    dot datetime default now()
);

select * from trigger1;
select * from trigger2;


DELIMITER $$
create trigger inserting
after INSERT on trigger1 
for each row
begin
insert into trigger2(messege) values("inserted succesfully");
end$$
delimiter;

insert into trigger1 value(1,"fxgfcv",234567);


DELIMITER$$
create trigger updating
after UPDATE on trigger1
for each row
begin
insert into  trigger2(messege) values("updated succesefully");
end$$
DELIMITER;


update trigger1 set name = "sameer" where id =1;

DELIMITER$$
create trigger errorss
before INSERT on trigger1
for each row
begin
if new.bal<0 THEN
SIGNAL SQLSTATE '45000' set MESSAGE_TEXT ="insufficient";
end if;
end $$
DELIMITER;

insert into trigger1 values(1,"acsa",-99);
