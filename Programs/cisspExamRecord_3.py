import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd


class DataCollectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CISSP模拟考试选择录入工具")
        self.root.geometry("500x350")

        # 存储所有收集的数据（使用字典存储，键为序号）
        self.data = {}
        # 当前序号（1-160）
        self.current_index = 1

        # 创建LabelFrame容器
        self.frame = tk.LabelFrame(root, text="数据录入", padx=10, pady=10)
        self.frame.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

        # ==================== 新增：序号编辑功能 ====================
        # 序号设置框架
        self.index_frame = tk.Frame(self.frame)
        self.index_frame.pack(fill=tk.X, pady=(0, 10))

        # 序号设置标签
        self.index_label = tk.Label(self.index_frame, text="当前序号:")
        self.index_label.pack(side=tk.LEFT, padx=(0, 5))

        # 序号输入框
        self.index_var = tk.StringVar(value=str(self.current_index))
        self.index_entry = tk.Entry(self.index_frame, textvariable=self.index_var, width=5)
        self.index_entry.pack(side=tk.LEFT, padx=(0, 10))

        # 设置序号按钮
        self.set_index_btn = tk.Button(self.index_frame, text="设置序号",
                                       command=self.set_start_index, width=10)
        self.set_index_btn.pack(side=tk.LEFT)
        # ==================== 新增结束 ====================

        # 选项选择标签
        self.lab2 = tk.Label(self.frame, text="请选择选项:")
        self.lab2.pack(fill=tk.X, pady=(0, 5))

        # 选项下拉菜单
        self.option_var = tk.StringVar()
        self.option_menu = ttk.Combobox(self.frame, textvariable=self.option_var,
                                        values=["A", "B", "C", "D"], state="readonly")
        self.option_menu.pack(fill=tk.X, pady=(0, 15))
        self.option_menu.current(0)  # 默认选择A

        # 状态标签
        self.status_label = tk.Label(self.frame, text="准备录入数据...", fg="gray")
        self.status_label.pack(fill=tk.X)

        # 按钮框架
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        # 确认按钮
        self.confirm_btn = tk.Button(self.button_frame, text="确认",
                                     command=self.confirm_selection, width=10)
        self.confirm_btn.pack(side=tk.LEFT, padx=(0, 10))

        # 导出当前数据按钮
        self.export_btn = tk.Button(self.button_frame, text="导出当前数据",
                                    command=self.export_current_data, width=12)
        self.export_btn.pack(side=tk.LEFT, padx=(0, 10))

        # 最终保存按钮（初始禁用）
        self.save_btn = tk.Button(self.button_frame, text="最终保存",
                                  command=self.save_to_excel, state=tk.DISABLED, width=10)
        self.save_btn.pack(side=tk.LEFT)

    def set_start_index(self):
        """设置起始序号功能[6,7](@ref)"""
        try:
            new_index = int(self.index_var.get())
            if 1 <= new_index <= 160:
                self.current_index = new_index
                self.status_label.config(text=f"已设置起始序号为: {self.current_index}", fg="green")
                # 更新界面显示
                self.index_var.set(str(self.current_index))

                # 如果之前已禁用组件，重新启用
                if self.current_index <= 160:
                    self.confirm_btn.config(state=tk.NORMAL)
                    self.option_menu.config(state="readonly")
                    self.save_btn.config(state=tk.DISABLED)
            else:
                messagebox.showwarning("无效序号", "序号必须在1-160范围内！")
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字序号！")

    def confirm_selection(self):
        """处理确认按钮点击事件[1](@ref)"""
        # 获取当前选项
        current_option = self.option_var.get()

        # 保存当前数据（使用字典存储，键为序号）
        self.data[self.current_index] = current_option
        self.status_label.config(text=f"已保存: {self.current_index} {current_option}", fg="green")

        # 更新索引
        self.current_index += 1

        # 检查是否达到上限
        if self.current_index > 160:
            self.index_var.set("160")
            self.status_label.config(text="已达到最大序号(160)，请点击'最终保存'按钮", fg="red")
            self.confirm_btn.config(state=tk.DISABLED)
            self.option_menu.config(state=tk.DISABLED)
            self.save_btn.config(state=tk.NORMAL)
        else:
            # 更新界面显示
            self.index_var.set(str(self.current_index))
            self.option_menu.current(0)  # 重置为默认选项

    def export_current_data(self):
        """导出当前已收集的数据到Excel[2](@ref)"""
        if not self.data:
            messagebox.showwarning("无数据", "当前没有可导出的数据！")
            return

        try:
            # 创建DataFrame（按序号排序）
            sorted_data = sorted(self.data.items(), key=lambda x: x[0])
            df = pd.DataFrame(sorted_data, columns=["考题序号", "我的选项"])

            # 弹出保存对话框
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel 文件", "*.xlsx"), ("所有文件", "*.*")],
                title="保存当前数据"
            )

            if not file_path:  # 用户取消保存
                return

            # 导出到Excel
            df.to_excel(file_path, index=False)

            # 更新状态
            self.status_label.config(text=f"已导出 {len(self.data)} 条数据到 {file_path}", fg="blue")
            messagebox.showinfo("导出成功", f"已成功导出 {len(self.data)} 条数据！")
        except Exception as e:
            self.status_label.config(text=f"导出失败: {str(e)}", fg="red")
            messagebox.showerror("导出错误", f"导出过程中发生错误:\n{str(e)}")

    def save_to_excel(self):
        """最终保存所有数据到Excel文件[5](@ref)"""
        try:
            # 创建完整的DataFrame（1-160所有序号）
            full_data = []
            for i in range(1, 161):
                value = self.data.get(i, "")  # 如果序号无数据则为空
                full_data.append((i, value))

            df = pd.DataFrame(full_data, columns=["序号", "选项"])

            # 导出到Excel
            filename = "data_final_export.xlsx"
            df.to_excel(filename, index=False)

            # 更新状态
            self.status_label.config(text=f"最终数据已成功导出到 {filename}", fg="blue")
            self.save_btn.config(state=tk.DISABLED)
            messagebox.showinfo("保存成功", f"160条数据已成功导出到 {filename}")
        except Exception as e:
            self.status_label.config(text=f"导出失败: {str(e)}", fg="red")
            messagebox.showerror("导出错误", f"导出过程中发生错误:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataCollectionApp(root)
    root.mainloop()