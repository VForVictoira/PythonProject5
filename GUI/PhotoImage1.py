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

image = Image.open('1.jpg')
image1 = ImageTk.PhotoImage(image)
label = Label(tk1, image=image1)
label.pack()
tk1.mainloop()