from tkinter import *

def msgShow():
    label.config(text='I love you',bg='lightyellow',fg='red')

root = Tk()
root.geometry('300x300')
root.title('LOVE')
label = Label(root)
btn = Button(root,text='I love you',command=msgShow)
label.pack()
btn.pack()
root.mainloop()
