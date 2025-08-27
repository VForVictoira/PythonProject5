from tkinter import *

from tkinter.ttk import *
import time

def running():
    for i in range(100):
        pb['value'] = i+1
        window.update()
        time.sleep(0.05)

window = Tk()
window.title('Progressbar_2')
window.geometry('300x300')

pb = Progressbar(window, orient=HORIZONTAL, length=300,mode='determinate')
pb.pack(fill=X, expand=1,padx=5,pady=5)
pb['maximum'] = 100
pb['value'] = 0

btn = Button(window, text='Running', command=running)
btn.pack(fill=BOTH, expand=1,padx=5,pady=5)
window.mainloop()

