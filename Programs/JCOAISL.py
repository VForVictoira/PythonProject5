import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, LabelFrame, PhotoImage
import webbrowser
import os
import ctypes


def add_host_entry():
    """添加hosts记录并验证管理员权限"""
    try:
        # 检查管理员权限
        if not ctypes.windll.shell32.IsUserAnAdmin():
            messagebox.showerror("权限错误", "需要管理员权限修改hosts文件")
            return False

        # 添加hosts记录
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
        entry = "192.168.200.20 jcoaisl.lab"

        with open(host_path, 'r+') as file:
            content = file.read()
            if entry not in content:
                file.write(f"\n{entry}\n")
        return True
    except Exception as e:
        messagebox.showerror("操作失败", f"hosts文件修改失败: {str(e)}")
        return False


def on_login():
    """登录按钮处理函数"""
    username = entry_username.get()
    password = entry_password.get()

    if username == "JCOA" and password == "JCOA@2025":
        if add_host_entry():
            root.destroy()
            webbrowser.open("https://jcoaisl.lab:8888")
    else:
        messagebox.showerror("登录失败", "用户名或密码错误")


def on_exit():
    """退出按钮处理函数"""
    root.destroy()


# 创建主窗口
root = tk.Tk()
root.title("JCOA Info-Sec Lab 登录系统")
root.geometry("300x500")
root.iconbitmap(r'D:\Coding\PythonProjects\PythonProject5\Programs\logo.ico')
# 创建Labelframe容器
labelframe = LabelFrame(root, padx=20, pady=20)
labelframe.pack(pady=20, padx=40, fill="both", expand=True)

try:
    # 加载图片 (替换为实际图片路径)
    logo = PhotoImage(file=r"D:\Coding\PythonProjects\PythonProject5\Programs\JCOA_logo4.png").subsample(2, 2)
    img_label = Label(labelframe, image=logo)
    img_label.image = logo  # 保持引用
    img_label.pack(pady=5)
except:
    # 图片加载失败时显示替代文本
    no_img_label = Label(labelframe, text="[LOGO]", font=("Arial", 24))
    no_img_label.pack(pady=10)

# 欢迎标签
welcome_label = Label(labelframe,
                      text="欢迎登录 JCOA Info-Sec Lab！",
                      font=("Microsoft YaHei", 9))
welcome_label.pack(pady=10)

# 用户名输入区域
username_frame = tk.Frame(root)
username_frame.pack(fill="x", padx=50, pady=5)

Label(username_frame, text="用户名:", font=("Arial", 11)).pack(side="left")
entry_username = Entry(username_frame, font=("Arial", 11))
entry_username.pack(side="right", expand=True, fill="x")

# 密码输入区域
password_frame = tk.Frame(root)
password_frame.pack(fill="x", padx=50, pady=10)

Label(password_frame, text="密　码:", font=("Arial", 11)).pack(side="left")
entry_password = Entry(password_frame, show="*", font=("Arial", 11))
entry_password.pack(side="right", expand=True, fill="x")

# 按钮区域
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

Button(button_frame, text="登录", command=on_login,
       width=10, font=("Arial", 10)).pack(side="left", padx=10)
Button(button_frame, text="退出", command=on_exit,
       width=10, font=("Arial", 10)).pack(side="right", padx=10)

root.mainloop()