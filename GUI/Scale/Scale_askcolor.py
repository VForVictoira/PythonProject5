from tkinter import *
from tkinter.colorchooser import *

def bgUpdate():
    # 更改窗口背景颜色
    myColor = askcolor() # 列出色彩对话框
    print(type(myColor),myColor)#打印传回值
    window.config(bg=myColor[1])#设定窗口背景颜色

window = Tk()
window.title("Scale_askcolor")
window.geometry("300x300")

btn = Button(window, text="Select Color", command=bgUpdate)
btn.pack()
window.mainloop()
