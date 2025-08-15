from tkinter import *
import random



window = Tk()
window.title("Hello World")


msgYes,msgNO,msgExit=1,2,3
def MessgeBox():
    msgType = random.randint(1,3)
    if msgType == msgYes:
        labTxt='YES'
    elif msgType == msgNO:
        labTxt='NO'
    elif msgType == msgExit:
        labTxt='EXIT'
    tl = Toplevel()
    tl.title("Message Box")
    tl.geometry("300x150")
    Label(tl,text=labTxt).pack(fill=BOTH,expand=1)

btn = Button(window,text='Click',relief=RAISED,command=MessgeBox)
btn.pack()

window.mainloop()