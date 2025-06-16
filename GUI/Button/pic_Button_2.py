from tkinter import *

def msgShow():
    label.config(text='I love you',bg='lightyellow',fg='red')

root = Tk()
root.geometry('300x300')
root.title('LOVE')
label = Label(root)

heart=PhotoImage(file='2.png')
btn = Button(root,image=heart,text='Click me',
             command=msgShow,compound=BOTTOM
             )
label.pack()
btn.pack(side=BOTTOM,anchor=S)
root.mainloop()
