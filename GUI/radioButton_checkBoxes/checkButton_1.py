from tkinter import *

window = Tk()
window.title('<UNK>')

lab = Label(window, text='选择喜欢的运动',
            fg='red',bg='green',width=20,height=2).grid(row=0)

var1 = IntVar()
cbtnNFL = Checkbutton(window, text='足球', variable=var1, onvalue=1, offvalue=0).grid(row=1,sticky=W)
var2 = IntVar()
cbtnMLB = Checkbutton(window, text='篮球', variable=var2, onvalue=1, offvalue=0).grid(row=2,sticky=W)
var3 = IntVar()
cbtnNBA = Checkbutton(window,text='棒球', variable=var3, onvalue=1, offvalue=0).grid(row=3,sticky=W)

window.mainloop()