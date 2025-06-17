# from tkinter import *
# root=Tk()
# root.title("calculator")
# root.geometry("350x400")





# ent=Entry(root,bg="black",fg="white",bd=10,width=30)
# ent.place(x=70,y=10)

# bt1=Button(root,text=" AC ",fg="black",bg="grey",bd=5)
# bt1.place(x=70,y=80)
# bt2=Button(root,text=" +/- ",fg="black",bg="grey",bd=5)
# bt2.place(x=125,y=80)
# bt3=Button(root,text="  %  ",fg="black",bg="grey",bd=5)
# bt3.place(x=180,y=80)
# bt4=Button(root,text="  /  ",fg="black",bg="orange",bd=5)
# bt4.place(x=235,y=80)



# bt5=Button(root,text="   7  ",fg="black",bg="grey",bd=5)
# bt5.place(x=70,y=130)
# bt6=Button(root,text="   8  ",fg="black",bg="grey",bd=5)
# bt6.place(x=125,y=130)
# bt7=Button(root,text="   9  ",fg="black",bg="grey",bd=5)
# bt7.place(x=180,y=130)
# bt8=Button(root,text="  x  ",fg="black",bg="orange",bd=5)
# bt8.place(x=235,y=130)



# bt9=Button(root,text="   4  ",fg="black",bg="grey",bd=5)
# bt9.place(x=70,y=180)
# bt10=Button(root,text="   5  ",fg="black",bg="grey",bd=5)
# bt10.place(x=125,y=180)
# bt11=Button(root,text="   6  ",fg="black",bg="grey",bd=5)
# bt11.place(x=180,y=180)
# bt12=Button(root,text="  -  ",fg="black",bg="orange",bd=5)
# bt12.place(x=235,y=180)


# bt13=Button(root,text="   1  ",fg="black",bg="grey",bd=5)
# bt13.place(x=70,y=230)
# bt14=Button(root,text="   2  ",fg="black",bg="grey",bd=5)
# bt14.place(x=125,y=230)
# bt15=Button(root,text="   3  ",fg="black",bg="grey",bd=5)
# bt15.place(x=180,y=230)
# bt16=Button(root,text="  + ",fg="black",bg="orange",bd=5)
# bt16.place(x=235,y=230)



# bt17=Button(root,text="   #  ",fg="black",bg="grey",bd=5)
# bt17.place(x=70,y=280)
# bt18=Button(root,text="   0  ",fg="black",bg="grey",bd=5)
# bt18.place(x=125,y=280)
# bt19=Button(root,text="   .   ",fg="black",bg="grey",bd=5)
# bt19.place(x=180,y=280)
# bt20=Button(root,text="  = ",fg="black",bg="orange",bd=5)
# bt20.place(x=235,y=280)
# root.mainloop()















from tkinter import *

def insert_number(num):
    ent.insert(END, str(num))

def add():
    ent.insert(END, '+')

def subtract():
    ent.insert(END, '-')

def multiply():
    ent.insert(END, 'x')

def divide():
    ent.insert(END, '/')

def clear():
    ent.delete(0, END)

def calculate():
    try:
        expression = ent.get().replace('x', '*')
        result = eval(expression)
        ent.delete(0, END)
        ent.insert(END, str(result))
    except:
        ent.delete(0, END)
        ent.insert(END, "Error")

  


root = Tk()
root.title("Calculator")
root.geometry("350x400")

ent = Entry(root, bg="black", fg="white", bd=10, width=25, font=('Arial', 14))
ent.place(x=30, y=10)

# Row 1
Button(root, text=" AC ", fg="black", bg="grey", bd=5, command=clear).place(x=70, y=80)
Button(root, text=" +/- ", fg="black", bg="grey", bd=5, ).place(x=125, y=80)
Button(root, text="  %  ", fg="black", bg="grey", bd=5, ).place(x=180, y=80)
Button(root, text="  /  ", fg="black", bg="orange", bd=5, command=divide).place(x=235, y=80)

# Row 2
Button(root, text="   7  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(7)).place(x=70, y=130)
Button(root, text="   8  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(8)).place(x=125, y=130)
Button(root, text="   9  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(9)).place(x=180, y=130)
Button(root, text="  x  ", fg="black", bg="orange", bd=5, command=multiply).place(x=235, y=130)

# Row 3
Button(root, text="   4  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(4)).place(x=70, y=180)
Button(root, text="   5  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(5)).place(x=125, y=180)
Button(root, text="   6  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(6)).place(x=180, y=180)
Button(root, text="  -  ", fg="black", bg="orange", bd=5, command=subtract).place(x=235, y=180)

# Row 4
Button(root, text="   1  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(1)).place(x=70, y=230)
Button(root, text="   2  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(2)).place(x=125, y=230)
Button(root, text="   3  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(3)).place(x=180, y=230)
Button(root, text="  + ", fg="black", bg="orange", bd=5, command=add).place(x=235, y=230)

# Row 5
Button(root, text="   #  ", fg="black", bg="grey", bd=5, command=lambda: None).place(x=70, y=280)
Button(root, text="   0  ", fg="black", bg="grey", bd=5, command=lambda: insert_number(0)).place(x=125, y=280)
Button(root, text="   .  ", fg="black", bg="grey", bd=5, command=lambda: insert_number('.')).place(x=180, y=280)
Button(root, text="  = ", fg="black", bg="orange", bd=5, command=calculate).place(x=235, y=280)

root.mainloop()
