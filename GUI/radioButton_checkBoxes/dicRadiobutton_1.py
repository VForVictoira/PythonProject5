from tkinter import *

def  printSelecton():
    print(cities[var.get()])

window = Tk()
window.title("<UNK>")

cities = {0:'广州', 1:'上海', 2:'北京', 3:'长沙', 4:'深圳',5:'石家庄'}
var = IntVar()
label = Label(window, text='最牛马的城市：', fg='red',
              width=20, height=1,
              bg='white').grid(row=0, column=0)
for val,city in cities.items():
    Radiobutton(window, text=city, variable=var, value=val, command=printSelecton).grid(row=val+1, column=0, sticky=W)
window.mainloop()