from tkinter import *

def msfShow():
    label['text'] = 'I love you'
    label['fg'] = 'lightyellow'
    label['bg'] = 'red'
    
root = Tk()
root.geometry('300x300')
root.title('LOVE')
label = Label(root)
btn = Button(root,text='PRINT',command=msfShow)
label.pack()
btn.pack()
root.mainloop()