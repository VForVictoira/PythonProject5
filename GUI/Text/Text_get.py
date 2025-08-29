from tkinter import *




def selectText():
        print('INSERT',text.index(INSERT))
        print('selectionstart:',text.index(CURRENT))
        print('selectionend:',text.index(END))


window=Tk()
window.geometry("300x300")
window.resizable(0,0)


btn =Button(window,text='Print Selection',command=selectText)
btn.pack()

text = Text(window)
text.pack(fill=BOTH,expand=1,padx=5,pady=5)


window.mainloop()