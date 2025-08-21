from tkinter import *
def  buttonClicked(event):
    print("clicked")
def  toggle(onoff):
    if var.get() == True:
        onoff.bind("<Button-1>", buttonClicked)
    else:
        onoff.unbind("<Button-1>")

window = Tk()
window.title("unbind_1")
window.geometry("300x300")

btn = Button(window, text="Click Me")
btn.pack()

var=BooleanVar()
cbtn = Checkbutton(window, variable=var,text='bind/unbind',command=lambda: toggle(btn))
cbtn.pack()
window.mainloop()