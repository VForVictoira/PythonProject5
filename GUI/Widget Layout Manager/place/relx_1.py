from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title("ch3 37")
root.geometry("640x480")

image2= Image.open('3.gif')
pic2=ImageTk.PhotoImage(image2)
lab2 =Label(root,image=pic2)
lab2.place(relx=0.1,rely=0.1,relheight=0.8)
root.mainloop()