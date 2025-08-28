from tkinter import *
from tkinter import messagebox

def newfile():
    messagebox.showinfo('New file','开新档案')

window = Tk()
window.title('Menu_1')
window.geometry('300x300')

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=menubar)

window.mainloop()