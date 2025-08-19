from tkinter import *

def printInfo():
    print(spin.get())

window = Tk()
window.title("Spinbox_1")
window.geometry("300x300")

spin = Spinbox(window, from_=0, to=30,increment=1,command=printInfo)
spin.pack(padx=5, pady=5)
window.mainloop()