from tkinter import *
root =Tk()
root.title("ch3 35_1")
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
lab1 = Label(root,text="Label 1",bg="pink")
lab2 = Label(root,text="Label 2",bg="lightblue")
lab3 = Label(root,bg="yellow")
lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+E+W)
root.mainloop()