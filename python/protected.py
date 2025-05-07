class person:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def _dispaly(self):
        print(self._name,self._age)


class student(person):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self._roll=roll

    def display(self):
        print(self._roll)


c=student("afu",20,2)
c.display() 
c._dispaly()    
                

