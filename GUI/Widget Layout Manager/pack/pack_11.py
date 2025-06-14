from tkinter import *

root=Tk()
root.geometry("300x100")
root.title("fill_2")
print('执行前',root.pack_slaves())
lab1=Label(root,text='OK',font='Times 20 bold',fg='red',bg='lightyellow')

lab1.pack(anchor=S,side=RIGHT,padx=10,pady=10)

lab2=Label(root,text='NO',font='Times 20 bold',fg='red',bg='lightyellow')

lab2.pack(anchor=S,side=RIGHT,padx=10,pady=10)

print('执行后',root.pack_slaves())
root.mainloop()