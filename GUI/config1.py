from tkinter import *
from PIL import ImageTk, Image


counter = 0
def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
    counting()


tk1 = Tk()
tk1.title("counter")
digit = Label(tk1,bg="yellow",fg="blue",height=2,width=2,font=("Arial",20,"bold"))
digit.pack()
run_counter(digit)
tk1.mainloop()


