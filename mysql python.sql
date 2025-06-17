show databases;

create database afsal;
use afsal;

create table person(
personID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255));


insert into person(personID,LastName,FirstName,Address,City)
values(1,"v","afsal","malappuram","malappuram"),(2,"m","hanan","mannarkkad","palakkad"),(3,"g","jiji","kollam","kerala")
	
show tables;

select * from person;
select personID,FirstName from person;

select * from person
where personID=2;

alter table person
add dob varchar(255);

show table person;

alter table person
drop column dob ;

alter table person
modify column dob int;


select * from person
where FirstName="afsal"and LastName="v";


select * from person
where FirstName="afsal"or LastName="m";

select * from person
where not FirstName="jiji";

select * from person
order by FirstName desc;

select * from person
order by LastName desc,FirstName asc;