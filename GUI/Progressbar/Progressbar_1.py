from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

window = Tk()
window.title('Progressbar_1')
window.geometry('300x300')


pb1 = ttk.Progressbar(window, orient=HORIZONTAL)
pb1.pack(padx=5,pady=5)
pb1['maximum'] = 100
pb1['value'] = 50

pb2 = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='determinate')
pb2.pack(padx=5,pady=5)
pb2['maximum'] = 100
pb2['value'] = 50

window.mainloop()