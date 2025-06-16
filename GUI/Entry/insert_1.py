from tkinter import *

def printInfo():
    print("Account:%s\nPassword:%s" % (accountE.get(),pwdE.get()))

window = Tk()
window.title('Entry')

msg='欢迎进入测试系统'
sseGif = PhotoImage(file='2.gif')
logo = Label(window, text=msg,image=sseGif,compound=BOTTOM)
accountL=Label(window, text='Account')
accountL.grid(row=1)
pwdL=Label(window, text='Password')
pwdL.grid(row=2)
buttonLogin = Button(window, text='Login',width=6,command=printInfo)
buttonR = Button(window, text='Register',width=6)
buttonExit = Button(window, text='Exit', width=6,command=window.destroy)
buttonLogin.grid(row=3,padx=15)
buttonR.grid(row=3,column=1,padx=15)
buttonExit.grid(row=3,column=2,padx=15)


logo.grid(row=0,columnspan=3,padx=10,pady=10)
accountE = Entry(window)
pwdE = Entry(window,show='*')

accountE.insert(0,'TEST')
pwdE.insert(0,'<PASSWORD>')

accountE.grid(row=1,column=1,columnspan=2)
pwdE.grid(row=2,column=1,columnspan=2,pady=10)
window.mainloop()