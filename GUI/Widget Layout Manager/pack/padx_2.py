from tkinter import *

window = Tk()
window.title("Side 1")
lab1=Label(window, text="测试文字1",bg="lightyellow")
lab2=Label(window, text="测试文字2",bg="lightgreen")
lab3=Label(window, text="测试文字3",bg="red")
lab1.pack(side=LEFT)
lab2.pack(side=LEFT,padx=10)
lab3.pack(side=LEFT)
window.mainloop()