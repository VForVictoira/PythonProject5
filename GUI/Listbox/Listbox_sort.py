from tkinter import *
def itemSorted():
    if(var.get() == True):
        revBool = True
    else:
        revBool = False
    listTmp = list(lb.get(0, END))
    sortedList = sorted(listTmp, reverse=revBool)
    lb.delete(0, END)
    for item in sortedList:
        lb.insert(END, item)
fruits = ['apple', 'banana', 'orange', 'apple']
window = Tk()
window.title("Listbox")
window.geometry("300x300")
lb = Listbox(window)
for fruit in fruits:
    lb.insert(END, fruit)
lb.pack()
btn = Button(window,text='Sort',command=itemSorted)
btn.pack()
var = BooleanVar()
cb = Checkbutton(window,variable=var,text='从大到小排序')
cb.pack()

window.mainloop()