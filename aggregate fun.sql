use afsal;


create table empp(
emppID int not null,
emppname varchar(255) not null,
salary varchar(255) not null,
primary key (emppID));


insert into empp(emppID,emppname,salary)
value(1,"afu",20000),(2,"hana",25000),(3,"jiji",30000),(4,"jaseer",280000),(5,"arju",300000);


select count(salary)
from empp;

select avg(salary)
from empp;

select sum(salary)
from empp;


select min(salary)
from empp;


select max(salary)
from empp;