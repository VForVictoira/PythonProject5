from tkinter import *

window = Tk()
window.title("row_column")
window.geometry("300x100")
lab1=Label(window, text="测试文字1",bg="lightyellow")
lab2=Label(window, text="测试文字2",bg="lightgreen")
lab3=Label(window, text="测试文字3",bg="red")
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=2)
lab3.grid(row=2,column=1)
window.mainloop()