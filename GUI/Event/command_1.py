from tkinter import *

def pythonClicked():
    if varPython.get():
        lab.config(text="Select Python")
    else:
        lab.config(text="Unselect Python")

def javaClicked():
    if varJava.get():
        lab.config(text="Select Java")
    else:
        lab.config(text="Unselect Java")

def buttonClicked():
    lab.config(text="Button clicked")

window = Tk()
window.title("command_1")
window.geometry("300x200")

frame = LabelFrame(window, text="Command_Test",relief=RIDGE, borderwidth=5, padx=5, pady=5)
frame.pack(padx=5, pady=5,anchor=CENTER, fill=X)

btn = Button(frame, text="Click Me", command=buttonClicked)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(frame, text="Python", variable=varPython,command=pythonClicked)
cbnPython.pack(anchor=W)

varJava = BooleanVar()
cbnJava = Checkbutton(frame, text="Java", variable=varJava,command=javaClicked)
cbnJava.pack(anchor=W)

lab = Label(window,bg="white",fg="black",height=2,width=12,font=("Times New Roman",20,"bold"))
lab.pack(anchor=S,fill=X)



window.mainloop()