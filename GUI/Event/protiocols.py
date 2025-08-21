from tkinter import *
from tkinter import messagebox

def callback():
    res = messagebox.askokcancel('OKCANCEL','结束或取消？')
    if res == True:
        window.destroy()
    else:
        return
window = Tk()
window.title("protocols")
window.geometry("300x300")

window.protocol("WM_DELETE_WINDOW", callback)

window.mainloop()