from tkinter.ttk import *
from tkinter import *

window = Tk()
window.title('Population Treeview')


list1=['芝加哥','800']
list2=['洛杉矶','1800']
list3=['南京','2800']

tree = Treeview(window,columns=('citites','populations'))
tree.heading('#0', text='State')
tree.heading('#1', text='City')
tree.heading('#2', text='Population')

tree.column('#1', anchor=CENTER,width=150)
tree.column('#2', anchor=CENTER,width=150)

tree.insert('','end',text='Ylino',values=list1)
tree.insert('','end',text='California',values=list2)
tree.insert('','end',text='Jiangsu',values=list3)
tree.pack()
window.mainloop()