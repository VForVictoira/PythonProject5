from tkinter import *


def printSelecton():
    num = var.get()
    if num == 1:
        label.config(text='你是男生')
    else:
        label.config(text='你是女生')

window = Tk()
window.title('radioButton_checkBoxes')
window.geometry('300x300')
var = IntVar()
var.set(1)
label = Label(window, text='这是预设，尚未选择',bg='lightyellow',width=30)
label.pack()
Radiobutton(window, text='测试1', variable=var, value=1,command=printSelecton,anchor=W).pack(side=LEFT)
Radiobutton(window, text='测试2', variable=var, value=2, command=printSelecton,anchor=W).pack(side=LEFT)
Radiobutton(window, text='测试11111', variable=var, value=3, command=printSelecton,anchor=W).pack(side=LEFT)

window.mainloop()
