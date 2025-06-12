from tkinter import *

window = Tk()
window.title("Side 1")
lab1=Label(window, text="测试文字1",bg="lightyellow")
lab2=Label(window, text="测试文字2",bg="lightgreen")
lab3=Label(window, text="测试文字3",bg="red")
lab1.pack(padx=50)
lab2.pack(padx=50)
lab3.pack(padx=50)
window.mainloop()