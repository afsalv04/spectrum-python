use afsal;


create table spectrum(
empID int not null,
empName varchar(255) not null,
dept varchar(255) not null,
salary varchar(255) not null,
place varchar(255) not null,
primary key(empID));
    
    drop table spectrum;
  insert into spectrum(empID,empName,dept,salary,place)
  value(1,"riju","python",22000,"malappuram"),(2,"ram","datascience",25000,"kannur"),(3,"raj","python",27000,"malappuram"),(4,"afu","python",30000,"malappuram"),(5,"hana","network",29000,"palakkad"),(6,"jiji","digi",26000,"kolam");
  
  
  select count(empID),place
  from spectrum
  group by place
  having count(place)>2;
  
  
   select sum(salary),empID
  from spectrum
  group by empID
  order by sum(salary)asc;
  
  select sum(salary),empID
  from spectrum
  group by empID
  order by sum(salary)asc
  having sum(salary)>25000