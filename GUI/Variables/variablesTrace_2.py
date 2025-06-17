from tkinter import *

def callback(*args):
    xL.set(xE.get())
    print('data changed',xE.get())

window = Tk()
window.title('trace')

xE = StringVar()
entry = Entry(window,textvariable=xE)
entry.pack(pady=5,padx=10)
xE.trace('w',callback)

xL = StringVar()
label = Label(window,textvariable=xL)
xL.set('同步显示')
label.pack(pady=5,padx=10)

window.mainloop()