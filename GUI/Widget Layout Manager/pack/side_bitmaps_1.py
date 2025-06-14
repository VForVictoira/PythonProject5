from tkinter import *

bitMaps=['error','hourglass','info','questhead','question','warning','gray12','gray25','gray50','gray75']
root = Tk()
root.title('side_bitmaps')

for bitM in bitMaps:
    Label(root, text=bitM,bitmap=bitM,fg='blue',
          font=('Arial',20,'bold')).pack(side=LEFT,padx=5,pady=5)
root.mainloop()