from tkinter import *

def msgShow():
    label.config(text='I love you',bg='lightyellow',fg='red')

root = Tk()
root.geometry('300x300')
root.title('LOVE')
label = Label(root)
btn1 = Button(root,text='PRINT',command=msgShow,width=15)
btn2 = Button(root,text='EXIT',command=root.destroy,width=15)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
root.mainloop()