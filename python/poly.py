# class dome:
#     def great(self,name=None):
#         if name:
#             print("hello")
#         else:
#             print("hello world")    

# r1=dome()
# r1.great()
# r1.great("afu")







# class parent:
#     def  show(self,name=None):
#         if name:
#             print("afsal")
#         else:
#             print("munna")

# c1=parent() 
# c1.show("afu")            





# overriding





class animal:
    def sound(self):
        print("animal make sound")



class dog(animal):
    def sound(self):
        print("bark")

class cat(animal):
    def sound(self):
        print("meow")  



a=animal()
a.sound()  


d=dog()
d.sound()



c=cat()
c.sound()

