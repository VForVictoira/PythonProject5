from tkinter import *

window = Tk()
window.title("OptionMenu_1")

var = StringVar(window)
optionmenu = OptionMenu(window,var,'Python','C++','Java','JavaScript')
optionmenu.pack()



window.mainloop()