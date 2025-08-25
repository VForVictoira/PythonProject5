from tkinter import *
def itemAdded():
    varAdd = entry.get()
    if(len(varAdd.strip()) == 0):
        return
    lb.insert(END, varAdd)
    entry.delete(0, END)

def itemRemoved():
    index = lb.curselection()
    if(len(index) == 0):
        return
    lb.delete(index)

window = Tk()
window.title("Listbox")
window.geometry("300x300")

entry = Entry(window)
entry.grid(row=0, column=0,padx=10, pady=10)

btnAdd = Button(window, text="Add", command=itemAdded)
btnAdd.grid(row=0, column=1)
btnRemove = Button(window, text="Remove", command=itemRemoved)
btnRemove.grid(row=2, column=0)

lb = Listbox(window)
lb.grid(row=1, column=0)
window.mainloop()