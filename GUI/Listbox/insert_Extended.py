from tkinter import *


window = Tk()
window.title("insert_1")
window.geometry("300x300")

fruits = ["apple", "banana", "cherry",
          "orange", "strawberry", "peach"]

lb = Listbox(window,selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack()


window.mainloop()