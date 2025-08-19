from tkinter import *

def printInfo():
    print('垂直尺度值 = %d,水平尺度值 = %d' % (sV.get(),sH.get()))
window = Tk()
window.title("Scale_3")

sV = Scale(window,label='垂直',from_=0,to=10)
sV.set(5)
sV.pack(anchor=E)
sH = Scale(window,label='水平',from_=0,to=10,orient=HORIZONTAL,length=300)
sH.set(3)
sH.pack()

Button(window,text='Print',command=printInfo).pack()

window.mainloop()