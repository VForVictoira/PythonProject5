from tkinter import *

def callback():
    print(lb.selection_includes(3))

window = Tk()
window.title("insert_1")
window.geometry("300x300")

fruits = ["apple", "banana", "cherry",
          "orange", "strawberry", "peach"]

lb = Listbox(window,selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack()

btn = Button(window, text="Click Me", command=callback)
btn.pack()

window.mainloop()