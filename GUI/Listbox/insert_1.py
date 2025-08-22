from tkinter import *


window = Tk()
window.title("insert_1")
window.geometry("300x300")

lb = Listbox(window)

lb.insert(END, "Apple")
lb.insert(END, "Banana")
lb.insert(END, "Pineapple")

lb.pack(fill=Y)


window.mainloop()