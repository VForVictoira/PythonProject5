from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Text Example")

text = Text(window,height=2,width=30)
text.pack(side=LEFT,fill=X)

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text.yview)

window.mainloop()