from Lib.tkinter.filedialog import asksaveasfile
from tkinter import *
from tkinter.filedialog import asksaveasfilename

def newFile():
    text.delete(1.0,END)
    window.destroy()

def saveAsFile():
    global filename
    textContent = text.get(1.0,END)
    filename = asksaveasfilename(defaultextension='.txt')
    if filename == '':
        return
    with open(filename,'w') as output:
        output.write(textContent)
        window.title(filename)
filename = 'Untitled'
window = Tk()
window.geometry('300x300')
window.title(filename)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Save', command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.destroy)
window.config(menu=menubar)

text = Text(window,undo=True)
text.pack(fill=BOTH, expand=True)

window.mainloop()
