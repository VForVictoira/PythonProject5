from tkinter import *
def cal():
    out.configure(text='结果：'+ str(eval(equ.get())))
window = Tk()
window.title('Calculator')
window.geometry('300x200')
label = Label(window,text='请输入数学表达式')
label.pack()
equ = Entry(window)
equ.pack(pady=5)

out = Label(window)
out.pack()

btn = Button(window,text='计算',command=cal)
btn.pack(pady=5)
window.mainloop()