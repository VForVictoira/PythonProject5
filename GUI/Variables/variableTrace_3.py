from tkinter import *

def callbackW(name,index,mode):
    xL.set(xE.get())
    print('name=%r,index=%r,mode=%r'%(name,index,mode))


window = Tk()
window.title('<UNK>')
xE = StringVar()

entry = Entry(window,textvariable=xE)
entry.pack(padx=5, pady=5)
xE.trace('w',callbackW)

xL = StringVar()
label = Label(window,textvariable=xL)
xL.set('同步显示')
label.pack(padx=5, pady=5)

window.mainloop()