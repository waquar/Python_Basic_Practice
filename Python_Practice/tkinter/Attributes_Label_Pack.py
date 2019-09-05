from tkinter import  *
root = Tk()
root.geometry("745x545")
root.title("waquar")                               #title of gui

#labels important
# text - adds the text
# bd-  background
#fg - foreground
#font - sets the font                 font= ("comicsansms", 10, "bold")   or "comicsansms 10 bold"
#padx- x padding
#pady - y padding
#relief - border styling - sunken,raised,groove,ridge

title_label = Label(text = """Shah Rukh Khan (born 2 November 1965), also known by the initialism SRK, is an Indian actor, \nfilm producer, and television personality. 
Referred to in the media as the "Badshah of Bollywood", "King of Bollywood" and "King Khan", 
\nhe has appeared in more than 80 Bollywood films, and earned numerous accolades, including 14 Filmfare Awards.
\n For his contributions to film, the Government of India honoured him with the Padma Shri, 
\nand the Government of France awarded him both the Ordre des Arts et des Lettres and the Légion d'honneur. \n
Khan has a significant following in Asia and the Indian diaspora worldwide. In terms of audience size and income, \n
he has been described as one of the most successful film stars in the world.
""" , bg='white', fg= 'red', padx = 67, pady = 94, font= ("comicsansms", 10, "bold"), borderwidth = 5, relief = SUNKEN)
title_label.pack()

#Important pack option
#anchor = nw   (anchor = "ne")
#side = top,bottom,left,right

title_label.pack(side = RIGHT,  fill = X, pady = 50)
root.mainloop()
