from tkinter import *

root = Tk()
root.title("keys")

label = Label(root,bg="lightyellow",fg="blue",relief=RAISED,
              padx=10,pady=10,
              cursor="heart"
              )
label.pack()
print(label.keys())
root.mainloop()