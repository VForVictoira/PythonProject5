from tkinter import *

def printInfo():
    print(spin.get())

window = Tk()
window.title("Spinbox_1")
window.geometry("300x300")
cities=('Singapore','New York','Shanghai')

spin = Spinbox(window,values=cities,
               command=printInfo)
spin.pack(padx=5, pady=5)
window.mainloop()