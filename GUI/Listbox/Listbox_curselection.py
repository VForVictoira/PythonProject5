from tkinter import *

def callback():
    indexs = lb.curselection()
    selected_items=[]
    for index in indexs:
        selected_items.append(lb.get(index))
        print(lb.get(index))
    var.set(','.join(selected_items))
 

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

x = '--'
var = StringVar()
text = "{}".format(x)
var.set(text)

lb1 = Label(window, textvariable=var,bg="light blue")
lb1.pack(fill=X)

window.mainloop()