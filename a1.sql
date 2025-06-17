create database StudentDB;

use StudentDB;

create table  Students(
stdID int not null,
stdname varchar(255) not null,
stdmail varchar(255) not null,
DOB date not null,
primary key (stdID));

insert into  Students(stdID,stdName,stdmail,DOB)
value(1,"afsal","afsal@gmail.com","2001-04-13"),(2,"hanan","hanan@gmail.com","2000-10-03"),(3,"jiji","jiji@gmail.com","1999-02-10");

select * from Students;

alter table Students
add phone varchar(255);

alter table Students
modify column stdname varchar(100); 

alter table Students
drop column phone;

drop table Students;


insert into  Students(stdID,stdName,stdmail,DOB)
value(1,"afsal","afsal@gmail.com","2001-04-13"),(2,"hanan","hanan@gmail.com","2000-10-03"),(3,"jiji","jiji@gmail.com","1999-02-10"),(
4,"ramu","ramu@gmail.com","2002-10-25"),(5,"raju","raju@gmail.com","2005-04-11"),(6,"zhalu","zhalu@gmail.com","2003-05-17");


select * from Students
where  DOB >"2000-01-01";


select stdName, stdmail from Students;


delete from Students 
where stdID=2;


delete from Students
where stdName like '%z%'
limit 1;


create table Mark(
StdID int not null,
Subj varchar(255),
Marks int not null,
primary key(StdID));

insert into Mark(StdID,SubJ,Marks)values(1,"English",40),(2,"Malayalam",80),(3,"Hindi",90),(4,"Calclus",90),(5,"graphics",90),(6,"DS",40),(7,"Physics",90),(8,"Chemistry",100),(9,"DS",40),(10,"flat",50)

select * from Mark;

select * from  Marks
where Mark>70;


select avg(Marks)
from Mark;

select min(Marks)
from Mark;

select max(Marks)
from Mark;


select * from Students
order by stdName asc;



select * from Students
where stdID in (1,3,5);