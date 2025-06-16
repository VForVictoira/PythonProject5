from tkinter import *

window = Tk()
window.title("fill_1")
window.geometry("300x100")
lab1=Label(window, text="测试文字1",bg="lightyellow")
lab2=Label(window, text="测试文字2",bg="lightgreen")
lab3=Label(window, text="测试文字3",bg="red")
lab1.pack(side=LEFT,fill=Y)
lab2.pack(side=LEFT,fill=BOTH,expand=1)
lab3.pack(side=LEFT,fill =Y)
window.mainloop()