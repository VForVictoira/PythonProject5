from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def msg():
    messagebox.showinfo('Message','Hello World')
window = Tk()
window.title('Notebook 1')
window.geometry('300x300')

notebook = Notebook(window)

frame1 = Frame()
frame2 = Frame()

label1 = Label(frame1,text='Python')
label1.pack(side=LEFT)
button1 = Button(frame1,text='Button 1',command=lambda:msg())
button1.pack(side=LEFT)

notebook.add(frame1,text='选项卡 1')

notebook.add(frame2,text='选项卡 2')
notebook.pack(fill=BOTH, expand=1,padx=5,pady=5)

window.mainloop()