from tkinter import *
root =Tk()
root.title("ch3 35")# 窗口标题
colors = ["red" ,"orange","yellow","green","blue","purple"]
r= 0
#row编号
for color in colors:
    Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(root,bg=color,relief="ridge",width=20).grid(row=r,column=1)
    r+= 1
root.mainloop()