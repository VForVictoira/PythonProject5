from tkinter import *

def calculate():
    result = eval(equ.get())
    equ.set(equ.get() + '=\n' + str(result))

def show(buttonString):
    content = equ.get()
    if content == '0':
        content = ''
    equ.set(content+buttonString)

def backspace():
    equ.set(str(equ.get()[:-1]))

def clear():
    equ.set('0')

window = Tk()
window.title("Calculator")
for i in range(5):
    window.rowconfigure(i, weight=1)
for c in range(3):
    window.columnconfigure(c, weight=1)
equ = StringVar()
equ.set('0')

# 设计显示区
Label(window, textvariable=equ,bg='gray',width=20).grid(row=0,column=0,columnspan=4)
Button(window,fg='blue',command=clear,text='C',width=3).grid(row=1,column=0,padx=5)
#清除显示区按钮
Button(window,text='DEL',width=3,command=backspace).grid(row=1,column=1,padx=5)
#其他按钮
btnpe = Button(window,text='%',width=3,command=lambda:show('%')).grid(row=1,column=2,padx=5)
btnL = Button(window,text='/',width=3,command=lambda:show('/')).grid(row=1,column=3,padx=5)
btn7 = Button(window,text='7',width=3,command=lambda:show('7')).grid(row=2,column=0,padx=5)
btn8 = Button(window,text='8',width=3,command=lambda:show('8')).grid(row=2,column=1,padx=5)
btn9 = Button(window,text='9',width=3,command=lambda:show('9')).grid(row=2,column=2,padx=5)
btnS = Button(window,text='+',width=3,command=lambda:show('+')).grid(row=2,column=3,padx=5)
btn4 = Button(window,text='4',width=3,command=lambda:show('4')).grid(row=3,column=0,padx=5)
btn5 = Button(window,text='5',width=3,command=lambda:show('5')).grid(row=3,column=1,padx=5)
btn6 = Button(window,text='6',width=3,command=lambda:show('6')).grid(row=3,column=2,padx=5)
btnD = Button(window,text='-',width=3,command=lambda:show('-')).grid(row=3,column=3,padx=5)
btn1 = Button(window,text='1',width=3,command=lambda:show('1')).grid(row=4,column=0,padx=5)
btn2 = Button(window,text='2',width=3,command=lambda:show('2')).grid(row=4,column=1,padx=5)
btn3 = Button(window,text='3',width=3,command=lambda:show('3')).grid(row=4,column=2,padx=5)
btnM = Button(window,text='*',width=3,command=lambda:show('*')).grid(row=4,column=3,padx=5)
btn0 = Button(window,text='0',width=10,command=lambda:show('0')).grid(row=5,column=0,columnspan=2,padx=5)
btnDt = Button(window,text='.',width=3,command=lambda:show('.')).grid(row=5,column=2,padx=5)
btnE = Button(window,text='=',width=3,command=calculate,bg='yellow').grid(row=5,column=3,padx=5)
window.mainloop()