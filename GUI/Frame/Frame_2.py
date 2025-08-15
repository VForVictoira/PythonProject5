from tkinter import *

window = Tk()
window.title("Frame_1")

fms = {'red':'cross','green':'boat','blue':'boat','yellow':'boat','purple':'boat'}

for fmColor in fms:
    Frame(window,bg=fmColor,cursor=fms[fmColor],
          height=50,width=250).pack(side=LEFT)

window.mainloop()