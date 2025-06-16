from tkinter import *

window = Tk()
window.title('Entry')

nameL=Label(window,text='Name')
nameL.grid(row=0)
addressL=Label(window,text='Address')
addressL.grid(row=1)

nameEn=Entry(window)
addressEn=Entry(window)
nameEn.grid(row=0,column=1)
addressEn.grid(row=1,column=1)

window.mainloop()