from tkinter import *

counter = 0
def run_counter(event):
    def counting():
        global counter
        counter += 1
        event.config(text=str(counter))
        event.after(1000, counting)
    counting()

root = Tk()
root.title("Button")
digit = Label(root, bg="red", fg="white",
              height=5, width=5,
              font=("Arial", 20, "bold"))
digit.pack()
run_counter(digit)
Button(root, text="End",width=10, command=root.destroy).pack(pady=10)
root.mainloop()
