from tkinter import  *
#variable classes in tkinter
#BooleanVar, DoubleVar, IntVar, StringVar

root = Tk()
root.geometry("576x378")
user = Label(root, text = "Username")
password = Label(root, text = "Password")
user.grid()                                                                                      #also used like pack
password.grid()


def login():
    print(uservalue.get())   #taken from text variable
    print(passvalue.get())

uservalue = StringVar()
passvalue = StringVar()
userentry = Entry(root, textvariable = uservalue)
passentry  = Entry(root, textvariable = passvalue)
userentry.grid(row = 0, column = 1)
passentry.grid(row = 1, column = 1)
Button(text = "Submit", command = login).grid()

root.mainloop()
