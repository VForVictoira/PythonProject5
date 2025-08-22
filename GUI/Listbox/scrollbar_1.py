from tkinter import *

window = Tk()
window.title("Listbox")

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

lb = Listbox(window, yscrollcommand=scrollbar.set)
for i in range(100):
    lb.insert(END, 'item'+str(i))
lb.pack(side=LEFT, fill=BOTH,expand=1)

scrollbar.config(command=lb.yview)
window.mainloop()