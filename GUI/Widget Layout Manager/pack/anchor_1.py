from tkinter import *

window = Tk()
window.title('anchor_1')
window.geometry('300x180')
oklabel1=Label(window,text='OK',font=('Arial',20,'bold'),
               fg='white',bg='blue'
               )
nolabel1=Label(window,text='NO',font=('Arial',20,'bold'),
               fg='white',bg='red')
oklabel1.pack(anchor=S,side=RIGHT,padx=10,pady=10)
nolabel1.pack(anchor=S,side=RIGHT,padx=10,pady=10)
window.mainloop()