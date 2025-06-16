from tkinter import *
window=Tk()
window.title("ch3 31")
lab1 = Label(window,text="明志工专",relief="raised")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科技大学",relief="raised")
lab4 = Label(window,bg="aqua",width=20)
lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5)
# 窗口标题
window.mainloop()