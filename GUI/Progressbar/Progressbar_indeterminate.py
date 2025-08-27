from tkinter import *
from tkinter.ttk import *
import time

def run():
    pb.start()
def stop():
    pb.stop()


window = Tk()
window.title("Progressbar_start_1")
window.geometry('500x200')

pb = Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
pb.pack(fill=X, expand=1)
pb['maximum'] = 100
pb['value'] = 0

btn = Button(window, text="Running",command=run)
btn.pack(fill=X, expand=1)

btn2 = Button(window, text="Stop",command=stop)
btn2.pack(fill=X, expand=1)
window.mainloop()