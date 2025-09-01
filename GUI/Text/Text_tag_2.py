from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font



def sizeSelected(event):
    f=Font(size=sizeVar.get())
    text.tag_config(SEL,font=f)

window=Tk()
window.title("Marks")
window.resizable(False, False)

toolbar =Frame(window,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=2)

sizeVar=IntVar()
size = Combobox(toolbar,width=10,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size['values'] = sizeFamily
size.current(8)
size.bind('<<ComboboxSelected>>',sizeSelected)
size.pack()

text=Text(window)
text.pack(fill=BOTH,expand=1,padx=2,pady=2)
text.insert('end',"Hello World\n")
text.insert('end',"Hello World\n")
text.insert('end',"Hello World\n")
text.insert('end',"Hello World\n")
text.insert('end',"Hello World\n")
text.focus_set()

window.mainloop()