from tkinter import *

def callback(event):
    x = event.x
    y = event.y
    textvar = "Mouse Location - x:{},y:{}".format(x,y)
    var.set(textvar)

window = Tk()
window.title("command_2")
window.geometry("300x200")

x,y = 0,0
var = StringVar()
text = "Mouse Location - x:{},y:{}".format(x,y)
var.set(text)


lab = Label(window,textvariable=var)
lab.pack(anchor=S,side=RIGHT)

window.bind("<Motion>", callback)

window.mainloop()