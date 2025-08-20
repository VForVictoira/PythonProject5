from tkinter import *
from tkinter import messagebox

def show_message_box(msg_type):
    # 根据传入的参数msg_type来决定弹出哪种对话框
    if msg_type == 'showinfo':
        messagebox.showinfo("Information", "This is an info message")
    elif msg_type == 'showwarning':
        messagebox.showwarning("Warning", "This is a warning")
    elif msg_type == 'showerror':
        messagebox.showerror("Error", "An error occurred!")
    elif msg_type == 'askquestion':
        response = messagebox.askquestion("Question", "Do you want to proceed?")
        print("User selected:", response)  # 这里会返回'yes'或'no'
    elif msg_type == 'askokcancel':
        response = messagebox.askokcancel("Confirmation", "Confirm action?")
        print("User ok?:", response)  # 返回True或False
    elif msg_type == 'askyesno':
        response = messagebox.askyesno("Yes/No", "Is this correct?")
        print("User said yes?:", response)  # 返回True或False
    elif msg_type == 'askyesnocancel':
        response = messagebox.askyesnocancel("Continue?", "Save before exit?")
        if response is None:
            print("User canceled")
        else:
            print("User chose:", 'Yes' if response else 'No')
    elif msg_type == 'askretrycancel':
        response = messagebox.askretrycancel("Retry", "Failed to connect. Retry?")
        print("User wants to retry?:", response)  # 返回True或False
window = Tk()
window.title("Message_2")
frame = LabelFrame(window, text="MessageBox Test")
frame.pack(anchor="center", padx=5, pady=5)
buttons = [
    ('showinfo', 'showinfo'),
    ('showwarning', 'showwarning'),
    ('showerror', 'showerror'),
    ('askquestion', 'askquestion'),
    ('askokcancel', 'askokcancel'),
    ('askyesno', 'askyesno'),
    ('askyesnocancel', 'askyesnocancel'),
    ('askretrycancel', 'askretrycancel')
]

for i, (btn_text, msg_type) in enumerate(buttons):
    # 前四个放在第一行（0行），后四个放在第二行（1行）
    row = i // 4  # 0-3为0行，4-7为1行
    col = i % 4   # 列号0,1,2,3
    btn = Button(frame, text=btn_text, command=lambda t=msg_type: show_message_box(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
