# mystr=("apple","banana","cherry")
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))



class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=mynumber()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



