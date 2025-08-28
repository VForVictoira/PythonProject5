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
window.title('Menu_2')
window.geometry('300x180')

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save File", command=saveFile)
filemenu.add_command(label="Save As File", command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="New File", command=newFile)
editMenu.add_command(label="Open File", command=openFile)
editMenu.add_separator()
editMenu.add_command(label="Save File", command=saveFile)
editMenu.add_command(label="Save As File", command=saveAsFile)
editMenu.add_separator()
editMenu.add_command(label="Exit", command=window.destroy)
window.config(menu=menubar)

window.mainloop()