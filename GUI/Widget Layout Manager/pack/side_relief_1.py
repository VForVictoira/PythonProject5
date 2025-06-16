from tkinter import *

Reliefs=['flat','sunken','groove','raised','ridge','solid']
root = Tk()
root.title('side_relief_1')

for ref in Reliefs:
    Label(root, text=ref,relief=ref,fg='blue',
          font=('Arial',20,'bold')).pack(side=LEFT,padx=5,pady=5)
root.mainloop()