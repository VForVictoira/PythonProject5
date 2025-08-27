from tkinter import *

window = Tk()
window.title("OptionMenu_1")

omTuple=('Python','C++','Java','JavaScript')
var=StringVar(window)
var.set(omTuple[1])
optionMenu=OptionMenu(window,var,*omTuple)
optionMenu.pack(side=LEFT)


window.mainloop()