# try:
#     result=[2,3,4]
#     print(result[2])
# except Exception:
#     print("exception occured")
    
    


# try:
#     x=10/0
# except:
#     print("execption occured")    






# try:
#     even=[2,3,4,5]
#     print(even[6])
# except Exception:
#     print("execption occured")




try:
    result=10/-3
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("not divisible by zero")
else:
    print("the result is",result)
finally:
    print("execaption completed")