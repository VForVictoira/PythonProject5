from tkinter import *

window = Tk()
window.title("Message_2")

var = StringVar()
var.set('这是一个测试文本内容，这是一个测试文本内容，这是一个测试文本内容')
msg = Message(window, textvariable=var,
              bg='yellow', fg='red'
              )
msg.pack(padx=10, pady=10)
window.mainloop()