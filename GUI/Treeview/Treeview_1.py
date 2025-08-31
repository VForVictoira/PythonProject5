from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Treeview")

tree = Treeview(window,columns=('cities'))

tree.heading('#0', text='State')
tree.heading('#1', text='City')

tree.insert('','end',text='Ylino',values='Toronto')
tree.insert('','end',text='California',values='Los Angeles')
tree.insert('','end',text='Jiangsu',values='Nanjing')

tree.pack()

window.mainloop()