from tkinter import *

def callback(*args):
    print('data changed',xE.get())

window = Tk()
window.title('trace')

xE = StringVar()
entry = Entry(window,textvariable=xE)
entry.pack(pady=5,padx=10)
xE.trace('w',callback)
window.mainloop()