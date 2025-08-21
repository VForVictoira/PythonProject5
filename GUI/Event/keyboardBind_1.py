from tkinter import *
from tkinter import messagebox


def leave(event):
    ret = messagebox.askyesno("keyboardBind_1","是否离开？")
    if ret == True:
        window.destroy()
    else:
        return
window = Tk()
window.title("keyboardBind_1")
window.geometry("300x300")

window.bind("<Escape>", leave)
lab = Label(window,text='测试 ESC 键',
            bg='blue', fg='white',
            )
lab.pack()
window.mainloop()