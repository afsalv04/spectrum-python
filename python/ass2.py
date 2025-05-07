
# x=21
# if x%2==0:
#     print("even")
# else:
#     print("odd")



    # x=input("enter the string")
    # print(x)


# x=input("enter the string")
# print(x[::-1])


# x=input("enter the string")
# print(type(x))

# x=int(input("enter the number"))
# print(type(x))




# str=input("enter the string")
# if (str[::-1]==str):
#     print("palindrom")
# else:
#     print("not palindrom")




# for x in range(1,11):
#     print(x)



# x=("apple","banana","cherry")
# y=enumerate(x)
# print(list(y))




# x=int(input("enter the number"))
# y=int(input("enter the number"))

# temp=x
# x=y
# y=temp

# print(x)
# print(y)




# year=int(input("enter the year"))
# if year % 4 ==0:
#     if year % 100==0:
#         if year % 400==0:
#             print("year is leap year")
#         else:
#             print("year is not leap year")
#     else:
#         print("year is leap year")
# else:
#     print("year is not leap year")        

        



# year=int(input("enter the year"))

# if(year % 400==0)or(year % 4==0 and year % 100 !=0):
#     print("year is leap year")
# else:
#     print("year is not leap year")





# x=int(input("enter the number"))
# if x%3==0 and  x%5==0:
#     print("fizzbuz")
# elif x%3==0:
#     print("fizz")
# elif x%5==0:
#     print("buzz")
# else:
#     print("none")





# num_1 = 10
# num_2 = 11
# print(num_1 % num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)




# num_1=7
# num_2 = 6
# print(num_1 < num_2)
# print(num_1 > num_2)
# print(num_1 <= num_2)
# print(num_1 >= num_2)
# print(num_1==num_2)





# num_1=3
# num_2 = 4
# print((num_1 < num_2) and (num_1 != num_2))
# print((num_2 >= num_1) or (num_1 > num_2))
# print(not (num_1 == num_2))


# i=1
# while (i<10):
#   i = i +1
#   print(i) 






# customer_num =5
# invoice_num =1212
# print("Invoice No(s):")
# while(customer_num >0):
#      print("INV -", invoice_num)
#      invoice_num = invoice_num +3
#      customer_num = customer_num -1




# total_sum=0
# for x in range(101,200):
#     if x %7==0:
#         total_sum+=x
#         print(total_sum)




# x=int(input("enter the number"))
# y=int(input("enter the number"))
# z=int(input("enter the number"))

# if (x>=y)and(x>=z):
#     largest=x
# elif(y>=x)and(y>=z):
#     largest=y
# else:
#     largest=z

# print(largest)




# l=int(input("enter the length"))
# w=int(input("enter the width"))

# area=l*w
# print("area is",area)

# perimeter=(l+w)*2
# print("perimetre is",perimeter)




num=int(input("enter the number"))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime number")
            break
    else:
        print("its a prime number")
else:
    print("not a prime number")




# num=int(input("enter the number"))
# for i in range(0,11):
#     if 
