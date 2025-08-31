from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Treeview")

Aisa={'中国':'北京','日本':'东京',
           '泰国':'曼谷','韩国':'首尔'
           }

Europe={'英国':'伦敦','德国':'柏林',
           '法国':'巴黎','荷兰':'阿姆斯特丹'}

tree = Treeview(window,columns='capitals')
tree.heading('#0',text='国家')
tree.heading('capitals',text='首都')

idAsia=tree.insert('','end',text='Aisa')
idEurope=tree.insert('','end',text='Europe')

for country in Aisa.keys():
    tree.insert(idAsia,'end',text=country,values=Aisa[country])

for country in Europe.keys():
    tree.insert(idEurope,'end',text=country,values=Europe[country])
tree.pack()
window.mainloop()