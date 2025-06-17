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



# from tkinter import *
# root=Tk()
# Checkbox1=IntVar()
# Checkbox2=IntVar()
# Button1=Checkbutton(root,text="Learning",variable=Checkbox1,onvalue=1,offvalue=0,height=3,width=12)
# Button2=Checkbutton(root,text="Tutorial",variable=Checkbox2,onvalue=1,offvalue=0,height=3,width=12)
# Button1.pack()
# Button2.pack()
# mainloop()




# from tkinter import *
# root=Tk()
# canvas=Canvas(root,bg="yellow",width=150,height=250)
# canvas.pack()
# line=canvas.create_line(70,150,140,5)
# root.geometry("350x250")
# root.title("python lobby")
# root.mainloop()



# from tkinter import *
# root=Tk()
# canvas=Canvas(root,bg="yellow",width=150,height=250)
# canvas.pack()
# line=canvas.create_line(70,150,140,5,20,15)
# root.geometry("350x250")
# root.title("python lobby")
# root.mainloop()



# from tkinter import *
# root=Tk()
# canvas=Canvas(root,bg="yellow",width=150,height=250)
# canvas.pack()
# rectangle=canvas.create_rectangle(30,20,50,90,fill="light green")
# root.geometry("350x400")
# root.title("python lobby")
# root.mainloop()



# from tkinter import *
# root=Tk()
# can=Canvas(root,bg="yellow",width=150,height=250)
# can.pack()
# oval=can.create_oval(20,30,60,110,fill="light green")
# root.geometry("350x400")
# root.title("python lobby")
# root.mainloop()



# from tkinter import *
# root=Tk()
# root.title("python lobby")
# radio1=StringVar(root,"2")
# bt1=Radiobutton(root,text="radio button 1",variable=radio1,value="1")
# bt1.pack()
# bt2=Radiobutton(root,text="radio button 2",variable=radio1,value="2")
# bt2.pack()
# bt3=Radiobutton(root,text="radio button 3",variable=radio1,value="3")
# bt3.pack()
# root.geometry("350x400")
# root.mainloop()



# from tkinter import *
# from tkinter import ttk
# root=Tk()
# listbox=Listbox(root,width=45,height=15,selectmode=MULTIPLE)
# listbox.pack(pady=20)
 
# listbox.insert(0,"c")
# listbox.insert(1,"c++")
# listbox.insert(2,"java")
# listbox.insert(3,"python")
# root.geometry("350x400")
# root.title("python lobby")
# root.mainloop()



# from tkinter import *
# root=Tk()
# def callback():
#     text = textbox.get(0.1,END)
#     print(text)
# textbox=Text(root,width=43,height=10)
# textbox.pack()

# bt=Button(root,text="display,text",command=callback)
# bt.pack(pady=12)
# root.geometry("350x400")
# root.title("python")
# root.mainloop()



# from tkinter import *
# root=Tk()
# textbox=Text(root,width=40,height=13,wrap=WORD)
# textbox.grid(row=0,column=0)

# scroll=Scrollbar(root,orient=VERTICAL,command=textbox.yview)
# scroll.grid(row=0,column=1,sticky=N+S)
# textbox.config(yscrollcommand=scroll.set)

# root.geometry("350x400")
# root.title("python")
# root.mainloop()
