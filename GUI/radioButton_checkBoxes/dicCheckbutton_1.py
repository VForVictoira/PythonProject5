from tkinter import *


def printInfo():
    selection = ''
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection = selection + sports[i] + '\t'
    print(selection)

window = Tk()
window.title('dicCheckbutton')


Label(window, text='请选择喜欢的运动').grid(row=0, column=0, sticky=W)
sports = {0: '篮球', 1: '足球', 2: '乒乓球', 3: '羽毛球'}
checkboxes = {}
for i in range(len(sports)):
    checkboxes[i] = BooleanVar()
    Checkbutton(window, text=sports[i], variable=checkboxes[i]).grid(row=i+1, column=0, sticky=W)
btn = Button(window, text='确定', command=printInfo).grid(row=i+2, column=0, sticky=W)

window.mainloop()
