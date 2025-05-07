# class parent:
#     def __init__(self,name):
#         self.__name=name

#     def __private(self):
#         print(self.__name)

#     def public1(self):
#         self.__private()

# c=parent("afs")
# c.public1()               





class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __private(self):
        print(self.__name,self.__age)

    def public(self):
        self.__private()

c1=student("afsal",20)
c1.public()                