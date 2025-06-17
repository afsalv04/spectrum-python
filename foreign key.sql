use afsal; 

create table comp(
compID int not null,
compname varchar(255) not null,
place varchar(255) not null,
compyear varchar(255) not null,
primary key(compID));


insert into comp(compID,compname,place,compyear)
value(1,"specturm","south",2001),(2,"stype","maradu",2004),(3,"luminar","kakkand",2002);



create table emp1(
emp1ID int not null,
emp1name varchar(255) not null,
salary varchar(255) not null,
compID int not null,
primary key (emp1ID),
foreign key(compID)references comp(compID)
);

drop table emp1;


insert into emp1(emp1ID,emp1name,salary,compID)
value(1,"afu",20000,2),(2,"hana",25000,1),(3,"jiji",30000,2),(4,"jaseer",280000,3);


select * from emp1;