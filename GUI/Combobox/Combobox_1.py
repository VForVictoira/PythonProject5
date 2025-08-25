from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Combobox_1")
window.geometry("300x300")
var = StringVar()
cb = Combobox(window, textvariable=var)
cb['value'] =('Python','C++')

cb.pack(side=LEFT)

window.mainloop()