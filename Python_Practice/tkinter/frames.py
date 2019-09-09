from tkinter import  *

root = Tk()
root.geometry("745x342")
f1 = Frame(root, bg = "grey", borderwidth = 6, relief = SUNKEN)         #used for making frame
f1.pack(side = LEFT, fill = "y")

f2 = Frame(root, bg = "grey", borderwidth = 6, relief = SUNKEN)         #used for making frame
f2.pack(side = RIGHT, fill = "y")

l1 = Label(f1, text = "waquar ")
l1.pack(pady = 42)

l2= Label(f2, text = "alam")
l2.pack(pady = 42)

root.mainloop()