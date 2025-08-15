from tkinter import *


window = Tk()
window.title("Frame_5")

fm = Frame(width=150, height=80,relief=RAISED,borderwidth=5)
fm.pack()
lab = Label(fm,text="复选常用语言")
lab.pack()


# 使用小写变量名并添加 anchor
python_checkbox = Checkbutton(fm, text='Python')
python_checkbox.pack(anchor=W)

java_checkbox = Checkbutton(fm, text='Java')  # 修正文本为 'Java'
java_checkbox.pack(anchor=W)

go_checkbox = Checkbutton(fm, text='Go')
go_checkbox.pack(anchor=W)

window.mainloop()

