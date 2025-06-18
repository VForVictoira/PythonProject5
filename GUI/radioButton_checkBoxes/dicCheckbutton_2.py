from tkinter import *
from tkinter import messagebox


def display_selection():
    """显示用户选择的运动项目"""
    try:
        # 收集所有选择的运动
        selected_sports = [sport for idx, sport in sports_dict.items() if checkbox_vars[idx].get()]

        if not selected_sports:
            result_label.config(text="您没有选择任何运动", fg="gray")
            return

        # 格式化显示结果
        result = "您选择的运动：\n" + "\n".join(selected_sports)
        result_label.config(text=result, fg="blue")

    except Exception as e:
        messagebox.showerror("错误", f"处理选择时出错: {e}")


# 创建主窗口
window = Tk()
window.title("运动选择器")
window.geometry("300x280")  # 设置初始窗口大小
#window.resizable(False, False)  # 禁止调整窗口大小

# 配置更美观的样式
window.configure(bg="#f0f0f0")  # 设置背景色
window.option_add("*Font", "Arial 10")  # 设置全局字体

# 运动选项字典
sports_dict = {
    0: '🏀 篮球',
    1: '⚽ 足球',
    2: '🏓 乒乓球',
    3: '🏸 羽毛球',
    4: '🎾 网球',
    5: '🎯 射击'
}

# 创建标题标签
title_label = Label(window,
                    text="请选择您喜欢的运动",
                    font=("Arial", 12, "bold"),
                    bg="#f0f0f0",
                    fg="#333")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 15), sticky=W)

# 使用Frame容器包裹复选框，提高布局稳定性
checkbox_frame = Frame(window, bg="#f0f0f0")
checkbox_frame.grid(row=1, column=0, columnspan=2, padx=15, pady=5, sticky=W)

# 存储复选框变量的字典
checkbox_vars = {}

# 创建复选框
for idx, sport in sports_dict.items():
    checkbox_vars[idx] = BooleanVar()
    chk = Checkbutton(checkbox_frame,
                      text=sport,
                      variable=checkbox_vars[idx],
                      bg="#f0f0f0",
                      activebackground="#e6f7ff",
                      padx=5,
                      pady=3)
    chk.grid(row=idx, column=0, sticky=W, pady=2)

# 结果显示标签
result_label = Label(window,
                     text="请选择后点击确定",
                     font=("Arial", 10),
                     bg="#f0f0f0",
                     fg="gray",
                     wraplength=280,
                     justify=LEFT)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=(15, 5), sticky=W)

# 按钮容器
button_frame = Frame(window, bg="#f0f0f0")
button_frame.grid(row=7, column=0, columnspan=2, pady=(5, 10))

# 确定按钮
submit_btn = Button(button_frame,
                    text="确定",
                    command=display_selection,
                    width=8,
                    bg="#4CAF50",
                    fg="white",
                    activebackground="#45a049")
submit_btn.pack(side=LEFT, padx=5)

# 退出按钮
exit_btn = Button(button_frame,
                  text="退出",
                  command=window.destroy,
                  width=8,
                  bg="#f44336",
                  fg="white",
                  activebackground="#d32f2f")
exit_btn.pack(side=LEFT, padx=5)

# 运行主循环
window.mainloop()