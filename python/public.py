class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show (self):
        print(self.name,self.age)


c=parent("afu",20)
c.show()         