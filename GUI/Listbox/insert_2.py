from tkinter import *


window = Tk()
window.title("insert_1")
window.geometry("300x300")

fruits = ["apple", "banana", "cherry"]

lb = Listbox(window)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack()


window.mainloop()