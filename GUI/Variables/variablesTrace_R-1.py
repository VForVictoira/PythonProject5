from tkinter import *

def callbackW(*args):
    xL.set(xE.get())

def callbackR(*args):
    print('Warning:数据被读取！')

def hit():
    print('读取数据：',xE.get())

window = Tk()
window.title('<UNK>')

xE = StringVar()

entry = Entry(window, textvariable=xE)
entry.pack(padx=5, pady=5)

xE.trace('w',callbackW)
xE.trace('w',callbackR)

xL = StringVar()
label = Label(window, textvariable=xL)
xL.set('同步显示')
label.pack(padx=5, pady=5)

btn = Button(window,text='读取',command=hit)
btn.pack(padx=5, pady=5)
window.mainloop()