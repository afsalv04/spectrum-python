use afsal;

create table persons(
ID int not null,
FirstName varchar(255) not null,
lastName varchar(255) not null,
age int not null,
primary key(ID));


insert into persons(ID,FirstName,LastName,age)
value(1,"afu","v",20),(2,"hanu","m",21),(3,"jijiu","g",24);

show tables;

select * from persons;