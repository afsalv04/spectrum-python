# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root123"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE store")








# import mysql.connector

# mydb= mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"
# )

# mycursor =  mydb.cursor()
# mycursor.execute("create table student(name varchar(255),address varchar(255))")







# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"
# )


# mycursor = mydb.cursor()

# sql = "insert into student(name,address) values(%s,%s)"
# val = [("afsal","malappuram"),
# ("hanan","palakkad"),
# ("jiji","kollam")]
# mycursor.executemany(sql,val)

# mydb.commit()





# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"
# )


# mycursor = mydb.cursor()
# mycursor.execute("select * from student")
# my=mycursor.fetchall()

# for x in my:
#     print(x)






# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"

# )

# mycursor=mydb.cursor()
# sql="select * from student where name = 'afsal'"
# mycursor.execute(sql)
# my=mycursor.fetchall()

# for x in my:
#     print(x)




# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"

# )

# mycursor=mydb.cursor()
# sql="select * from student ORDER BY address"
# mycursor.execute(sql)
# my=mycursor.fetchall()

# for x in my:
#     print(x)




# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"
# )

# mycursor=mydb.cursor()
# sql="delete from student where name = 'hanan'"
# mycursor.execute(sql)
# mydb.commit()




# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="store"
# )

# mycursor=mydb.cursor()
# sql="drop table student"
# mycursor.execute(sql)




import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="store"
)

mycursor=mydb.cursor()
sql= "UPDATE student SET address = 'mannarkkad' WHERE address = 'palakkad'"
mycursor.execute(sql)
mydb.commit()

