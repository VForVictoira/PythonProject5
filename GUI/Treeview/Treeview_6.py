from tkinter import *
from tkinter.ttk import *


def treeSelect(event):
    widgetObj=event.widget
    itemselected = widgetObj.selection()[0]
    col1 = widgetObj.item(itemselected,'text')
    col2 = widgetObj.item(itemselected,'values')[0]
    str = "{0}：{1}:{2}".format(col1,col2
    var.set(str)


window = Tk()
window.title("Treeview")

Aisa={'中国':'北京','日本':'东京',
           '泰国':'曼谷','韩国':'首尔'
           }

Europe={'英国':'伦敦','德国':'柏林',
           '法国':'巴黎','荷兰':'阿姆斯特丹'}

tree = Treeview(window,columns='capitals',selectmode='browse')
tree.heading('#0',text='国家')
tree.heading('capitals',text='首都')

idAsia=tree.insert('','end',text='Aisa',values=('',))
idEurope=tree.insert('','end',text='Europe',values=('',))
tree.tag_configure('b',background='red')
rowCount=1
for state in Aisa.keys():
    if (rowCount % 2 ==1):
        tree.insert(idAsia,'end',text=Aisa[state])
    else:
        tree.insert(idAsia,'end',text=Aisa[state],tags='b')
    rowCount += 1

for state in Europe.keys():
    if (rowCount % 2 ==1):
        tree.insert(idEurope,'end',text=Europe[state])
    else:
        tree.insert(idEurope,'end',text=Europe[state],tags='b')
    rowCount += 1

tree.bind('<<TreeviewSelect>>',treeSelect)
var = StringVar()
label = Label(window,textvariable=var,relief=SUNKEN)
label.pack(fill=BOTH,expand=1)

tree.pack()

window.mainloop()