from tkinter import *

window = Tk()
window.title("Frame_1")

for fm in ['red', 'green', 'blue']:
    Frame(window,bg=fm,height=50,width=250).pack(side=LEFT, padx=5)

window.mainloop()
