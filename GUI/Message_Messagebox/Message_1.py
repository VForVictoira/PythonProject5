from tkinter import *

window = Tk()
window.title("Message_1")
window.geometry("300x300")

mytext = '这是一个测试文本内容，这是一个测试文本内容，这是一个测试文本内容'
msg = Message(window, text=mytext,
              bg='yellow', fg='red'
              )
msg.pack(padx=10, pady=10)
window.mainloop()
