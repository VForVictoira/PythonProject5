from tkinter import *


window = Tk()
window.title("Frame_4")


fm1 = Frame(width=100, height=100,relief=GROOVE,borderwidth=5).pack(side=LEFT,padx=5,pady=10)
fm2 = Frame(width=100, height=100,relief=RAISED,borderwidth=5).pack(side=LEFT,padx=5,pady=10)
fm3 = Frame(width=100, height=100,relief=RIDGE,borderwidth=5).pack(side=LEFT,padx=5,pady=10)

window.mainloop()