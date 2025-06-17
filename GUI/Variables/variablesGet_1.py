from tkinter import *

def btn_hit():
   if x.get() == "":
       x.set('测试内容')
   else:
       x.set('')

window = Tk()
window.title('GET')

x = StringVar()

label = Label(window, textvariable=x,fg='blue',bg='lightyellow',font=('Arial',20,'bold'),
              width=20,height=2)
label.pack(pady=5)
btn = Button(window,text='click me',command=btn_hit)
btn.pack(pady=5)
window.mainloop()