from tkinter import *
from tkinter import messagebox


def  key(event):
    print('按了'+ repr(event.char)+'键')


window = Tk()
window.title("keyboardBind_2")
window.geometry("300x300")

window.bind("<Key>", key)
window.mainloop()