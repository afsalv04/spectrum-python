use afsal;

create table student(
stdID int not null,
stdname varchar(255) not null,
stdmark varchar(255) not null,
primary key(stdID));

insert into student(stdID,stdname,stdmark)
value(1,"ramu",90),(2,"raju",88),(3,"afu",89),(5,"jiji",88);

drop table student;

create table department(
deptname varchar(255) not null,
courses varchar(255) not null,
stdID int not null);

drop table department;

insert into department(deptname,courses,stdID)
value("cse","data science",2),("ec","desing",1),("me","fluids",3),("cse","python",4);


select s.stdname,d.courses
from student s
inner join department d on s.stdID=d.stdID;

select s.stdname,d.courses,deptname
from student s
left join department d on s.stdID=d.stdID;

select s.stdname,d.courses,deptname
from student s
right join department d on s.stdID=d.stdID;

select s.stdname,d.courses,deptname
from student s
cross join department d ;
