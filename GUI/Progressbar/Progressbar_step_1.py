from tkinter import *
from tkinter.ttk import *
import time

def running():
    while pb.cget('value') <= pb['maximum']:
        pb.step(2)
        window.update()
        print(pb.cget('value'))
        time.sleep(0.05)

window = Tk()
window.title("Progressbar_step_1")
window.geometry('500x300')

pb = Progressbar(window, orient=HORIZONTAL,length=200,mode='determinate')
pb.pack(fill=X, expand=1)
pb['maximum'] = 100
pb['value'] = 0

btn = Button(window, text="Running",command=running)
btn.pack(fill=X, expand=1)
window.mainloop()