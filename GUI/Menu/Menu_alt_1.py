from tkinter import *
from tkinter import messagebox

def newFile():
    messagebox.showinfo('New File','新健档案')

def openFile():
    messagebox.showinfo('New File','打开文档')

def saveFile():
    messagebox.showinfo('New File','保存文档')

def saveAsFile():
    messagebox.showinfo('New File','另存为')

window = Tk()
window.title('Menu_1')
window.geometry('300x300')

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu,underline=0)
filemenu.add_command(label="New File", command=newFile,underline=0)
filemenu.add_command(label="Open File", command=openFile,underline=0)
filemenu.add_separator()
filemenu.add_command(label="Save File", command=saveFile,underline=0)
filemenu.add_command(label="Save As File", command=saveAsFile,underline=5)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy,underline=0)
window.config(menu=menubar)
window.mainloop()