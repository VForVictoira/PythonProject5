from tkinter import *

window = Tk()
window.title("Side 1")
lab1=Label(window, text="测试文字1",bg="lightyellow")
lab2=Label(window, text="测试文字2",bg="lightgreen")
lab3=Label(window, text="测试文字3",bg="red")
lab1.pack(pady=10)
lab2.pack(pady=10)
lab3.pack(fill=X)
window.mainloop()