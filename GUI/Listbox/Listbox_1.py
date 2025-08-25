from tkinter import *


window = Tk()
window.title("Listbox_1")
window.geometry("300x300")

lb1 = Listbox(window)
lb1.pack(side=LEFT)
lb2 = Listbox(window,height=10,relief=SUNKEN)
lb2.pack(side=LEFT, anchor=N)

window.mainloop()