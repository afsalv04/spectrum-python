# x=lambda a,b: a+b
# print(x(2,5))




# x=[1,2,3,4]
# result=map(lambda a: a**2,x)
# print(list(result))




# x=[1,2,3,4]
# result=filter(lambda a: a%2==0,x)
# print(list(result))



# x=[1,2,3,4]
# result=map(lambda a: a**2,filter(lambda a: a%2==0,x))
# print(list(result))




from functools import reduce
num=[1,2,3,4]
total=reduce(lambda x,y: x+y,num)
print(total)