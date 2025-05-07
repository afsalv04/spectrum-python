# from tkinter import *

# root=Tk()
# root.title("welcome afsal")
# root.geometry('300x200')
# def clicked():
#     print("Iam Clicked")


# name="we are in specturam lobby"
# lab=Label(root, text=name, font=("Helvetica",12), fg="white", bg="black")
# lab.pack()

# lab=Label(root, text="Hi Iam AFSAL", font=("Helvetica",12), fg="white", bg="black")
# lab.pack()

# bt=Button(root, text="click",command=clicked, fg="red", bg="black", borderwidth=10)
# bt.pack(pady=10)


# entry=Entry(root,bg="yellow",fg="red",bd=5)
# entry.pack()


# root.mainloop() 



# from tkinter import *

# root=Tk()
# root.title("Login")
# root.geometry('300x200')
# def clicked():
#     print("iam clicked")


# lab=Label(root, text="UserName", font=("Helvetica",12), fg="white", bg="black")
# lab.place(x=0,y=4)
# entry=Entry(root,bg="yellow",fg="red",bd=5)
# entry.place(x=90,y=4)

# lab1=Label(root, text="Password", font=("Helvetica",12), fg="white", bg="black")
# lab1.place(x=0,y=43)
# entry1=Entry(root,bg="yellow",fg="red",bd=5)
# entry1.place(x=90,y=40)

# bt=Button(root, text="click",command=clicked, fg="red", bg="black", borderwidth=5)
# bt.place(x=100,y=80)



# root.mainloop()




# from tkinter import *

# root=Tk()
# root.title("Login")
# root.geometry('300x200')

# lab=Label(root, text="lobby", font=("Helvetica",12), fg="white", bg="black")
# lab.pack()

# frm=Frame(root,bg="green",width=120,height=100)
# frm.pack(side=LEFT,padx=20)

# frm=Frame(root,bg="yellow",width=120,height=100)
# frm.pack(side=LEFT,padx=40)

# root.mainloop()





# from tkinter import *
# from tkinter import ttk

# root=Tk()
# root.title("lobby")


# path=PhotoImage(file="diamond.png")
# lab=Label(root,image=path,width=400,height=400)
# lab.pack()
# root.mainloop()



from tkinter import *
root=Tk()


Checkbox1=IntVar()
Checkbox2=IntVar()

Button1=Checkbutton(root,text="Learning",variable=Checkbox1,onvalue=1,offvalue=0,height=3,width=12)

Button2=Checkbutton(root,text="Tutorial",variable=Checkbox2,onvalue=1,offvalue=0,height=3,width=12)


Button1.pack()
Button2.pack()
mainloop()