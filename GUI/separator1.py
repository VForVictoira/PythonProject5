from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("separator")

myTitle = '测试'
myContent = '测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试'

lab1 = Label(root, text=myTitle,font=('Arial',20,'bold'))
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=5)

lab2 = Label(root,text=myContent,bg="lightyellow",fg="blue",relief=RAISED,
              padx=10,pady=10,
              cursor="heart"
              )
lab2.pack(padx=10,pady=10)
root.mainloop()