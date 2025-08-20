from tkinter import *
from tkinter import messagebox

def myMesg1():
    ret = messagebox.askretrycancel('test1','安装失败，再试一次？')
    print('安装失败',ret)
def myMesg2():
    ret = messagebox.askyesnocancel('test2','编辑完成，是或否或取消？')
    print('编辑完成',ret)

window = Tk()
window.title("Message_Messagebox Box")
window.geometry("300x150")

Button(window,text="安装失败",command=myMesg1).pack(side=LEFT)
Button(window,text="编辑完成",command=myMesg2).pack(side=LEFT)

window.mainloop()