from tkinter import *

root = Tk()
root.title("Sign in to X")
root.geometry("400x500")
root.configure(bg="#15202b")  

x_label = Label(root, text="X", font=("Arial", 28, "bold"), fg="white", bg="#15202b")
x_label.pack(pady=20)

title = Label(root, text="Sign in to X", font=("Arial", 16, "bold"), fg="white", bg="#15202b")
title.pack(pady=10)

google_btn = Button(root, text="Sign in with Google", font=("Arial", 10), bg="white", fg="black", width=30, pady=10)
google_btn.pack(pady=5)


apple_btn = Button(root, text="Sign in with Apple", font=("Arial", 10), bg="white", fg="black", width=30, pady=10)
apple_btn.pack(pady=5)

or_label = Label(root, text="or", font=("Arial", 10), fg="gray", bg="#15202b")
or_label.pack(pady=10)


entry = Entry(root, font=("Arial", 12), width=30, bg="#192734", fg="white", bd=2, insertbackground="white")
entry.insert(0, "Phone, email address, or username")
entry.pack(pady=10)


next_btn = Button(root, text="Next", font=("Arial", 10), bg="white", fg="black", width=30, pady=10)
next_btn.pack(pady=5)


forgot_btn = Button(root, text="Forgot password?", font=("Arial", 10), bg="black", fg="white", width=30, pady=10, bd=1, relief="solid")
forgot_btn.pack(pady=5)


signup_label = Label(root, text="Don’t have an account? Sign up", font=("Arial", 9), fg="blue", bg="gray")
signup_label.pack(pady=20)

root.mainloop()