# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show (self):
#         print(self.name,self.age)

# class child(parent):
#     pass
# r1=child("afsal",20)
# r1.show()




# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show (self):
#         print(self.name,self.age)

# class child(parent):
#     pass
      
# r1=child("hanan",22)
# r1.show()               


# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show (self):
#         print(self.name,self.age)

# class child(parent):
#     def __init__(self,roll_no):
#         self.roll_no=roll_no
#     def shows (self):
#         print(self.roll_no)
      
# r1=child(3)
# r1.shows()   

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
    

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

# x = Student("Mike", "Olsen",5)
# x.printname()





# class collage:
#     def __init__(self,clg_id,clg_name):
#         self.clg_id=clg_id
#         self.clg_name=clg_name
#     def show (self):
#         print(self.clg_id,self.clg_name)    

# class student(collage):
#     # def __init__(self,name,id):
#     #     self.name=name
#     #     self.id=id
#     # def shows (self):
#     #     print(self.name,self.id)  
#     pass         

# r1=student(1,"mbg")
# r1.show()






# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show (self):
#         print(self.name,self.age)


# class child(parent):
#     pass

# r1=child("hanu",20)
# r1.show()


# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show (self):
#         print(self.name,self.age)


# class child(parent):
#     def __init__(self,name,age):
#     #     self.name=name
#     #     self.age=age
#     # def shows (self):
#     #     print(self.name,self.age)

# r1=child("afu",18)
# r1.shows()            










class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show (self):
        print(self.name,self.age)


class child(parent):
    def __init__(self,name,age):
         super().__init__(name,age)

r1=child("afu",18)
r1.show()