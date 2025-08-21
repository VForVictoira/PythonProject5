from tkinter import *
from tkinter import filedialog, messagebox  # 单独导入子模块
from tkinter import ttk
import pandas as pd


class DataCollectionApp:
    def __init__(self):
        # 创建主窗口
        self.root = Tk()
        self.root.title("数据采集工具")
        self.root.geometry("450x300")

        # 初始化数据存储
        self.data = []
        self.current_index = 1

        # 创建界面组件
        self.create_widgets()

        # 启动主循环
        self.root.mainloop()

    def create_widgets(self):
        """创建所有界面组件"""
        # 主容器
        self.frame = LabelFrame(self.root, text="数据录入", padx=10, pady=10)
        self.frame.pack(padx=15, pady=15, fill=BOTH, expand=True)

        # 序号标签
        self.lab1 = Label(self.frame, text="当前序号:")
        self.lab1.pack(fill=X, pady=(0, 5))

        self.index_label = Label(self.frame, text=str(self.current_index),
                                 font=("Arial", 12, "bold"), fg="blue")
        self.index_label.pack(fill=X, pady=(0, 10))

        # 选项选择框
        self.lab2 = Label(self.frame, text="请选择选项:")
        self.lab2.pack(fill=X, pady=(0, 5))

        self.option_var = StringVar()
        self.option_menu = ttk.Combobox(self.frame, textvariable=self.option_var,
                                        values=["A", "B", "C", "D"], state="readonly")
        self.option_menu.pack(fill=X, pady=(0, 15))
        self.option_menu.current(0)  # 默认选择A

        # 状态标签
        self.status_label = Label(self.frame, text="准备录入数据...", fg="gray")
        self.status_label.pack(fill=X)

        # 按钮区域
        self.button_frame = Frame(self.root)
        self.button_frame.pack(fill=X, padx=15, pady=(0, 15))

        # 确认按钮
        self.confirm_btn = Button(self.button_frame, text="确认",
                                  command=self.confirm_selection, width=10)
        self.confirm_btn.pack(side=LEFT, padx=(0, 10))

        # 导出按钮
        self.export_btn = Button(self.button_frame, text="导出当前数据",
                                 command=self.export_current_data, width=12)
        self.export_btn.pack(side=LEFT, padx=(0, 10))

        # 最终保存按钮
        self.save_btn = Button(self.button_frame, text="最终保存",
                               command=self.save_to_excel, state=DISABLED, width=10)
        self.save_btn.pack(side=LEFT)

    def confirm_selection(self):
        """处理确认按钮点击事件"""
        current_option = self.option_var.get()
        self.data.append((self.current_index, current_option))
        self.status_label.config(text=f"已保存: {self.current_index} {current_option}", fg="green")

        # 更新索引
        self.current_index += 1

        # 检查上限
        if self.current_index > 160:
            self.index_label.config(text="160", fg="red")
            self.status_label.config(text="已达到最大序号(160)，请点击'最终保存'按钮", fg="red")
            self.confirm_btn.config(state=DISABLED)
            self.option_menu.config(state=DISABLED)
            self.save_btn.config(state=NORMAL)
        else:
            self.index_label.config(text=str(self.current_index))
            self.option_menu.current(0)

    def export_current_data(self):
        """导出当前数据到Excel"""
        if not self.data:
            messagebox.showwarning("无数据", "当前没有可导出的数据！")
            return

        try:
            df = pd.DataFrame(self.data, columns=["序号", "选项"])
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel 文件", "*.xlsx"), ("所有文件", "*.*")],
                title="保存当前数据"
            )

            if file_path:
                df.to_excel(file_path, index=False)
                self.status_label.config(text=f"已导出 {len(self.data)} 条数据到 {file_path}", fg="blue")
                messagebox.showinfo("导出成功", f"已成功导出 {len(self.data)} 条数据！")
        except Exception as e:
            self.status_label.config(text=f"导出失败: {str(e)}", fg="red")
            messagebox.showerror("导出错误", f"导出过程中发生错误:\n{str(e)}")

    def save_to_excel(self):
        """最终保存所有数据"""
        try:
            df = pd.DataFrame(self.data, columns=["序号", "选项"])
            filename = "data_final_export.xlsx"
            df.to_excel(filename, index=False)
            self.status_label.config(text=f"最终数据已成功导出到 {filename}", fg="blue")
            self.save_btn.config(state=DISABLED)
            messagebox.showinfo("保存成功", f"160条数据已成功导出到 {filename}")
        except Exception as e:
            self.status_label.config(text=f"导出失败: {str(e)}", fg="red")
            messagebox.showerror("导出错误", f"导出过程中发生错误:\n{str(e)}")


# 启动应用程序
if __name__ == "__main__":
    DataCollectionApp()