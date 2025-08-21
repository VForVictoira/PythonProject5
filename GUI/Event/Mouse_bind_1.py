from tkinter import *

def callback(event):
    print("Clicked at", event.x, event.y)

window = Tk()
window.title("command_2")
window.geometry("300x200")

frame = Frame(window,width=300,height=200)
frame.bind("<Motion>", callback)
frame.pack()
window.mainloop()