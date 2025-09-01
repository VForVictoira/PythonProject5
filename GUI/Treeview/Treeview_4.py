from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Treeview")

stateCity={'安徽':'合肥','湖南':'长沙',
           '广东':'广州','湖北':'武汉'
           }

tree = Treeview(window,columns='cities')
tree.heading('#0',text='State')
tree.heading('cities',text='City')

tree.column('cities',anchor=CENTER)

tree.tag_configure('evenColor',background='light blue')
rowCount = 1
for state in stateCity.keys():
    if (rowCount % 2 == 1) :
        tree.insert('','end',text=state,values=stateCity[state])
    else:
        tree.insert('','end',text=state,values=stateCity[state],
                    tags=('evenColor'))
    rowCount += 1
tree.pack()

window.mainloop()