from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title("ch3 37")
root.geometry("640x480")
image1= Image.open('2.gif')
pic1=ImageTk.PhotoImage(image1)
lab1 =Label(root,image=pic1)
lab1.place(x=20,y=30,width=200,height=120)
image2= Image.open('3.gif')
pic2=ImageTk.PhotoImage(image2)
lab2 =Label(root,image=pic2)
lab2.place(x=200,y=200,width=400,height=240)
root.mainloop()