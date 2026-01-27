show DATABASES;
use college;
create table courses (c_id int primary key , c_name varchar(20),dur INT);
create table students(stu_id int primary key , stu_name VARCHAR(30),d_join date ,c_id int,constraint forgien_college FOREIGN KEY (c_id)references courses(c_id));

alter table courses drop constraint forgien_college ;
SHOW CREATE TABLE students;

ALTER TABLE students
DROP FOREIGN KEY forgien_college;

DROP table students;
INSERT INTO courses VALUES
(1, 'Python', 6),
(2, 'Java', 5),
(3, 'AI', 8);

INSERT INTO students VALUES
(101, 'Rahul', '2025-01-10', 1),
(102, 'Anita', '2025-02-15', 2),
(103, 'Sameer', '2025-03-01', 3);


