from tkinter import *

def callback(event):
    obj = event.widget
    index = obj.curselection()
    var.set(obj.get(index))

window = Tk()
window.title("insert_1")
window.geometry("300x300")

fruits = ["apple", "banana", "cherry",
          "orange", "strawberry", "peach"]

lb = Listbox(window,selectmode=EXTENDED)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack()
lb.bind("<<ListboxSelect>>", callback)

var = StringVar()
label = Label(window, text='--',textvariable=var)
label.pack()



window.mainloop()