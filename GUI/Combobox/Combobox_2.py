from tkinter import *
from tkinter.ttk import *


def comboSelection(event):
    labelVar.set(var.get())
window = Tk()
window.title("Combobox_1")
window.geometry("300x300")
var = StringVar()
cb = Combobox(window, textvariable=var)
cb['value'] =('Python','C++')
cb.current(0)
cb.bind('<<ComboboxSelected>>', comboSelection)
cb.pack(side=LEFT)

labelVar = StringVar()
label = Label(window, textvariable=labelVar)
labelVar.set(var.get())
label.pack(side=LEFT)

window.mainloop()