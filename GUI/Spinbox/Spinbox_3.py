from tkinter import *

def printInfo():
    print(spin.get())

window = Tk()
window.title("Spinbox_1")
window.geometry("300x300")

spin = Spinbox(window,values=(10,38,170,101),
               command=printInfo)
spin.pack(padx=5, pady=5)
window.mainloop()