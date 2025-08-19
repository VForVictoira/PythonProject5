from tkinter import *

window = Tk()
window.title("Scale_2")

slider = Scale(window,
               from_=0,
               to=10,
               troughcolor='light blue',
               width=30,
               tickinterval=2,
               label='My Scale',
               length=300,
               orient=HORIZONTAL)
slider.pack()

window.mainloop()