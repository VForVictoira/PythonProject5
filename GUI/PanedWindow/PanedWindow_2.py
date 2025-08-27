from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Add Host")

pw = PanedWindow(orient=HORIZONTAL)

leftframe = LabelFrame(pw,text='Left Frame',width=140,height=150)
pw.add(leftframe,weight=1)
middleframe = LabelFrame(pw,text='Middle Frame',width=120)
pw.add(middleframe,weight=1)
rightframe = LabelFrame(pw,text='Right Frame',width=140,height=150)
pw.add(rightframe,weight=1)

pw.pack(fill=X, expand=1,padx=5,pady=5)

pw2 = PanedWindow(orient=HORIZONTAL)

leftframe2 = LabelFrame(pw2,text='Left Frame2',width=140,height=150)
pw2.add(leftframe2,weight=1)
middleframe2 = LabelFrame(pw2,text='Middle Frame2',width=120)
pw2.add(middleframe2,weight=1)
rightframe2 = LabelFrame(pw2,text='Right Frame2',width=140,height=150)
pw2.add(rightframe2,weight=1)

pw2.pack(fill=X, expand=1,padx=5,pady=5)


window.mainloop()