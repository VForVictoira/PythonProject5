from tkinter import *
from tkinter import messagebox


def minizaIcon():
    window.iconify()
def showPopuMenu(event):
    popumenu.post(event.x_root, event.y_root)

window = Tk()
window.geometry("300x300")

popumenu = Menu(window, tearoff=0)
popumenu.add_command(label="Miniza", command=minizaIcon)
popumenu.add_command(label="Exit", command=window.destroy)
window.bind('<Button-3>',showPopuMenu)

window.mainloop()