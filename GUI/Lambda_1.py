from idlelib import window
from tkinter import *

def bColor(bgColor):
    root.config(bg=bgColor)

root = Tk()
root.title("Button_5")
root.geometry("300x300")
exitbtn = Button(root, text="Exit", command=root.destroy)
yellowbtn = Button(root, text="Yellow", comman=lambda:bColor('yellow'))
bluebtn = Button(root, text="Blue", comman=lambda:bColor('blue'))

exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()