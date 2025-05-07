# f=open("demofile.txt","x")


# with open("demofile.txt","w") as f:
#     f.write("my name is afsal")



# with open("demofile.txt","r") as f:
#     print(f.read())




# with open("demofile.txt","r") as f:
#     print(f.read(8))




# list=["hello world\n","welcome to python\n","file handling is easy\n"]
# with open("demofile.txt","w") as f:
#     f.writelines(list)



# with open("demofile.txt","r") as f:
#     print(f.read())


# with open("demofile.txt","r") as f:
#     print(f.readline())



# with open("demofile.txt","r") as f:
#     print(f.readlines())



# with open ("demofile.txt","a") as f:
#     f.write("my name is afu")    
    



   

# f=open("newcsv.csv","x")

# import csv

# with open("newcsv.csv","w",newline='') as f:
#     w=csv.writer(f)
#     w.writerow(["afsal","movie","kochi"])
#     w.writerow(["hanan","play","ernakulam"])
#     w.writerow(["arjun","food","malappuram"])
       
# import csv
# with open("newcsv.csv","r")as f:
#     r=csv.reader(f)

#     for row in r:
#         print(row)




# f=open("myfile.zip","x")

# import zipfile

# with zipfile.ZipFile("myfile.zip","w") as f:
#     f.write("newcsv.csv")
#     f.write("demofile.txt")





import zipfile

with zipfile.ZipFile("myfile.zip","r") as f:
    f.extractall("afsal")
    list1=f.namelist()
    print(list1)