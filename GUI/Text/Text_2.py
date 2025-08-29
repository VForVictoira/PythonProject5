from tkinter import *
window = Tk()


xscrollbar = Scrollbar(window,orient=HORIZONTAL)
yscrollbar = Scrollbar(window,orient=VERTICAL)

text=Text(window,height=5,width=30)
xscrollbar.pack(side=BOTTOM, fill=Y)
yscrollbar.pack(side=RIGHT, fill=Y)
text.pack(fill=BOTH, expand=1)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
text.config(xscrollcommand=xscrollbar.set,yscrollcommand=yscrollbar.set)

window.mainloop()