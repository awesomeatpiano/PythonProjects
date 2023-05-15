#cindy 
#gui practice
#5/15/23

from tkinter import *

root = Tk()

root.title("im watching you")
root.geometry("500x500")

app = Frame(root)
app.grid()

lbl = Label(app,text = "hola")
lbl.grid()

bttn1 = Button(app, text = "click for nothing.")
bttn1.grid()

root.mainloop()