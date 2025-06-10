from tkinter import *
from PIL import ImageTk, Image

tk1 = Tk()
tk1.title("label1")
screen_width = tk1.winfo_screenwidth()
screen_height = tk1.winfo_screenheight()
w = 300
h = 300
x = (screen_width - w) / 2
y = (screen_height - h) / 2
tk1.geometry("%dx%d+%d+%d" % (w, h, x, y))

text1 = '测试测试测试'
gif = PhotoImage(file='2.gif')
label = Label(tk1, text=text1,image=gif,bg='lightyellow',compound=LEFT)
label.pack()
tk1.mainloop()
