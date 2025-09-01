from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Treeview")

tree = Treeview(window,columns=('cities','population'))

list1=['芝加哥','800']
list2=['洛杉矶','1800']
list3=['南京','2800']

tree.heading('#0', text='State')
tree.heading('#1', text='City')
tree.heading('#2', text='Population')

tree.insert('','end',text='Ylino',values=list1)
tree.insert('','end',text='California',values=list2)
tree.insert('','end',text='Jiangsu',values=list3)

tree.pack()

window.mainloop()