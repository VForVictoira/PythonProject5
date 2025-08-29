from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox

from numpy import size


def familyChanged(event):
    f=Font(family=familyVar.get())
    text.config(font=f)

def weightChanged(event):
    f=Font(weight=weightVar.get())
    text.config(font=f)

def sizeChanged(event):
    f=Font(size=sizeVar.get())
    text.config(font=f)


window = Tk()
window.title("Family")
window.resizable(width=0, height=0)

toolbar = Frame(window,relief=SUNKEN,borderwidth=1,background="#f0f0f0")
toolbar.pack(side=TOP, fill=X,padx=5,pady=5)


familyVar = StringVar()
familyFamily = ('Arial','Times New Roman','Courier New')
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily, command=familyChanged)
family.pack(side=LEFT,pady=2)

weightVar = StringVar()
weightFamily = ('normal','bold')
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily, command=weightChanged)
weight.pack(side=LEFT,pady=2)

font = Label(toolbar,text="Font Size")
font.pack(side=LEFT,pady=2)

sizeVar = IntVar()
size = Combobox(toolbar,values=size,textvariable=sizeVar)
sizeFamily=[x for x in range(8,30)]
size['value'] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeChanged)
size.pack(side=LEFT,pady=2)


text = Text(window)
text.pack(fill=BOTH, expand=1,padx=2,pady=2)
text.focus_set()

window.mainloop()