from tkinter import *

def btn_hit():
    global msg_on
    if msg_on == False:
        msg_on = True
        x.set('测试内容')
    else:
        msg_on = False
        x.set('11')

window = Tk()
window.title('GET')

msg_on = False
x = StringVar()

label = Label(window, textvariable=x,fg='blue',bg='lightyellow',font=('Arial',20,'bold'),
              width=20,height=2)
label.pack(pady=5)
btn = Button(window,text='click me',command=btn_hit)
btn.pack(pady=5)
window.mainloop()