from idlelib import window
from tkinter import *

def yellow():
    root.config(bg="yellow")       # 仅修改背景色
    root.title("Yellow Window")
   # 正确设置窗口标题的方法

def blue():
    root.config(bg="blue")
    root.title("Blue Window")


root = Tk()
root.title("Button_5")
root.geometry("300x300")
exitbtn = Button(root, text="Exit", command=root.destroy)
yellowbtn = Button(root, text="Yellow", command=yellow)
bluebtn = Button(root, text="Blue", command=blue)

exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()