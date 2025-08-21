from tkinter import *

def btnClicked1():
    print("Command event handler")
def btnClicked2(event):
    print("Bind event handler")


window = Tk()
window.title("unbind_1")
window.geometry("300x300")

btn = Button(window, text="Button 1", command=btnClicked1)
btn.pack()
btn.bind("<Button-1>", btnClicked2,add="+")

window.mainloop()