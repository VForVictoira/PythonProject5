from tkinter import *

def getIndex(event):
    lb.index = lb.nearest(event.y) # 目前选项的索引

def dragJob(event):
    newIndex = lb.nearest(event.y)
    if newIndex < lb.index:
        x = lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex+1, x)
        lb.index=newIndex
    elif newIndex > lb.index:
        x = lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex-1, x)
        lb.index=newIndex


fruits = ['apple', 'banana', 'orange', 'ape']
window = Tk()
window.title("Listbox")
window.geometry("300x300")
lb = Listbox(window)
for fruit in fruits:
    lb.insert(END, fruit)
    lb.bind('<Button-1>', getIndex)
    lb.bind('<B1-Motion>', dragJob)
lb.pack()


window.mainloop()