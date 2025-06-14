from tkinter import *
window =Tk()
window.title("ch3 36")
# 窗口标题
lab1 =Label(window,text="明志科技大学",bg="lightyellow",width=15)

lab2 = Label(window,text="长庚大学",bg="lightgreen",width=15)
lab3 = Label(window,text="长庚科技大学",bg="lightblue",
            width=15)
lab1.place(x=0,y=0)
lab2.place(x=30,y=50)
lab3.place(x=60,y=100)
window.mainloop()