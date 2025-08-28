from tkinter import *

def status():
    if demoStatus.get():
        statusLabel.pack(side=BOTTOM,fill=X)
    else:
        statusLabel.pack_forget()

window = Tk()
window.title('checkbutton')
window.geometry('300x200')

menubar = Menu(window)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Exit', command=window.destroy)

viewMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='View', menu=viewMenu)
demoStatus = BooleanVar()
demoStatus.set(True)
viewMenu.add_checkbutton(label='Status', variable=demoStatus,command=status)
window.config(menu=menubar)

statusVar = StringVar()
statusVar.set('显示')
statusLabel = Label(window, textvariable=statusVar,relief=SUNKEN)
statusLabel.pack(side=BOTTOM,fill=X)
window.mainloop()