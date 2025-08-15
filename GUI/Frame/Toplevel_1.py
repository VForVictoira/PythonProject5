from tkinter import *

window = Tk()
window.title("Toplevel")

tl = Toplevel()
tl.title("Toplevel")
tl.geometry("300x200")
Label(tl,text="Hello World").grid(row=0,column=0)

window.mainloop()