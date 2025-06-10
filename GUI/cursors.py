from tkinter import *

root = Tk()
root.title("cursor")

label = Label(root,bg="lightyellow",fg="blue",relief=RAISED,
              padx=10,pady=10,
              cursor="heart"
              )
label.pack()
root.mainloop()