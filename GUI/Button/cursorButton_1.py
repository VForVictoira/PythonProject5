from tkinter import *
def msgShow():
    label.config(text='LOVE',bg='red',fg='white')

root = Tk()
root.geometry('300x300')
root.title('Hello World')
label = Label(root)
heart = PhotoImage(file='2.png')
btn = Button(root,image=heart,text='Click me',command=msgShow,
             cursor='heart',compound=TOP)

label.pack()
btn.pack(side=TOP,anchor=S)
root.mainloop()

