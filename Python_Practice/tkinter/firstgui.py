from tkinter import  *
from PIL import Image, ImageTk                                   #used pillow for other formats

root = Tk()
# widthxheight in geometry
root.geometry("744x524")                        #size of widget
root.minsize(320,240)                                 #width,height                        min,max used to lock the size
root.maxsize(800,560)

waquar = Label(text = "waquar created this!")
waquar.pack()                                                                  #used to display the label

#used default tkinter photo picker
# photo = PhotoImage(file="1.png")
# waq_photo = Label(image = photo)
# waq_photo.pack()

#below to use pil
image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)
waq_photo = Label(image = photo)
waq_photo.pack()

root.mainloop()


