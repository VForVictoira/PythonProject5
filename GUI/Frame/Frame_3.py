from tkinter import *


window = Tk()
window.title("Frame_3")



frameUpper = Frame(window,bg='lightyellow')
frameUpper.pack()


btnRed = Button(frameUpper,text='Red',bg='red').pack(side=LEFT,padx=5,pady=5)
btnGreen = Button(frameUpper,text='Green',bg='green').pack(side=LEFT,padx=5,pady=5)
btnYellow = Button(frameUpper,text='Yellow',bg='yellow').pack(side=LEFT,padx=5,pady=5)

frameLower = Frame(window,bg='lightblue')
frameLower.pack()

btnPurple=Button(frameLower,text='Purple',bg='purple').pack(side=LEFT,padx=5,pady=5)

window.mainloop()