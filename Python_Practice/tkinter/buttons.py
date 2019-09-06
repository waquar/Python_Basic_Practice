from tkinter import  *
root = Tk()
root.geometry("789x567")
frame = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN)
frame.pack(side =LEFT, anchor = "nw")

def hello():
    print("hello waquar")

b1 = Button(frame, fg = "red", text="waquar")
b1.pack(side = LEFT)
b2 = Button(frame, fg = "red", text="alam")
b2.pack(side = RIGHT)
b3 = Button(frame, fg = "red", text="ansari", command = hello)             #only give function name, dont call
b3.pack()


root.mainloop()