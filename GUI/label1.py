from tkinter import *

tk1 = Tk()
tk1.title("label1")
screen_width = tk1.winfo_screenwidth()
screen_height = tk1.winfo_screenheight()
w = 300
h = 300
x = (screen_width - w) / 2
y = (screen_height - h) / 2
tk1.geometry("%dx%d+%d+%d" % (w, h, x, y))

label= Label(tk1, bitmap='question',
              relief=SOLID, bg='lightblue',
             padx=10,pady=10,
              compound='left',text='label1')

'''label = Label(tk1, text="aasdasd",fg="red",bg="yellow",
              height=3,width=20,anchor=SW,
              wraplength=80,justify='right',
              font=('TimesNewRoman', 13,'bold')
              )'''
label.pack()
print(type(label))
tk1.mainloop()