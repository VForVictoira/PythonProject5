from tkinter.ttk import *
from tkinter import *

def load():
    pb['value'] = 0
    pb['maximum'] = maxbytes
    loading()
def loading():              # 仿真下载数据
    global bytes
    bytes += 500            # 模拟每次下载 500B
    pb['value'] = bytes     # 设置指针
    if bytes < maxbytes:
        pb.after(50, loading) # 经过0.05s继续执行 loading

window = Tk()
window.title('Progressbar_3')
window.geometry('300x300')
bytes=0
maxbytes=10000

pb = Progressbar(window, length=200, mode='determinate',orient=HORIZONTAL)
pb.pack(fill=X, expand=1)
pb['value'] = 0

btn = Button(window, text='Loading', command=load)
btn.pack(fill=X, expand=1)

window.mainloop()