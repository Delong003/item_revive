from tkinter import messagebox
import tkinter as tk


class ItemReviveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("物品复活软件")  # 设置窗口标题
        self.root.geometry("250x300")  # 设置窗口的初始大小

        self.items = {}  # 用于存储物品信息的字典

        # 创建用户界面组件
        self.name_label = tk.Label(root, text="物品名称:")  # 创建物品名称标签
        self.name_label.grid(row=0, column=0, sticky="w")  # 布局物品名称标签

        self.name_entry = tk.Entry(root)  # 创建物品名称输入框
        self.name_entry.grid(row=0, column=1, sticky="ew")  # 布局物品名称输入框

        self.desc_label = tk.Label(root, text="物品描述:")  # 创建物品描述标签
        self.desc_label.grid(row=1, column=0, sticky="w")  # 布局物品描述标签

        self.desc_entry = tk.Entry(root)  # 创建物品描述输入框
        self.desc_entry.grid(row=1, column=1, sticky="ew")  # 布局物品描述输入框

        self.contact_label = tk.Label(root, text="联系信息:")  # 创建联系信息标签
        self.contact_label.grid(row=2, column=0, sticky="w")  # 布局联系信息标签

        self.contact_entry = tk.Entry(root)  # 创建联系信息输入框
        self.contact_entry.grid(row=2, column=1, sticky="ew")  # 布局联系信息输入框

        self.add_button = tk.Button(
            root, text="添加物品", command=self.add_item)  # 创建添加物品按钮
        self.add_button.grid(row=3, column=0)  # 布局添加物品按钮

        self.delete_button = tk.Button(
            root, text="删除物品", command=self.delete_item)  # 创建删除物品按钮
        self.delete_button.grid(row=3, column=1)  # 布局删除物品按钮

        self.show_button = tk.Button(
            root, text="显示所有物品", command=self.show_items)  # 创建显示所有物品按钮
        self.show_button.grid(row=4, column=0)  # 布局显示所有物品按钮

        self.search_button = tk.Button(
            root, text="查找物品", command=self.search_item)  # 创建搜索物品按钮
        self.search_button.grid(row=4, column=1)  # 布局搜索物品按钮

        self.items_listbox = tk.Listbox(
            root, height=10)  # 创建用于显示物品列表的Listbox组件
        self.items_listbox.grid(
            row=5, column=0, columnspan=2, sticky="ew")  # 布局Listbox组件

    def add_item(self):
        # 添加物品信息
        name = self.name_entry.get()  # 获取输入的物品名称
        description = self.desc_entry.get()  # 获取输入的物品描述
        contact = self.contact_entry.get()  # 获取输入的联系信息

        if name and description and contact:
            self.items[name] = {"description": description,
                                "contact": contact}  # 将物品信息存储在字典中
            messagebox.showinfo("物品复活软件", f"成功添加物品: {name}")  # 显示成功添加的提示信息
        else:
            messagebox.showwarning("警告", "所有字段均为必填项。")  # 输入不完整时显示警告信息

    def delete_item(self):
        # 删除指定的物品信息
        name = self.name_entry.get()  # 获取输入的物品名称

        if name in self.items:
            del self.items[name]  # 从字典中删除指定物品
            messagebox.showinfo("物品复活软件", f"成功删除物品: {name}")  # 显示成功删除的提示信息
        else:
            messagebox.showwarning("警告", "物品未找到。")  # 物品未找到时显示警告信息

    def show_items(self):
        # 显示所有物品信息
        self.update_items_listbox()  # 更新Listbox内容以显示所有物品

    def search_item(self):
        # 搜索并显示指定的物品信息
        name = self.name_entry.get()  # 获取输入的物品名称
        self.items_listbox.delete(0, tk.END)  # 清空Listbox以准备显示搜索结果

        if name in self.items:
            item = self.items[name]
            self.items_listbox.insert(
                tk.END, f"{name}: {item['description']}, {item['contact']}")  # 显示符合搜索条件的物品信息
        else:
            self.items_listbox.insert(tk.END, "未找到匹配的物品。")  # 未找到匹配物品时显示提示信息

    def update_items_listbox(self):
        # 更新Listbox，显示所有物品信息
        self.items_listbox.delete(0, tk.END)  # 清空Listbox
        for name, info in self.items.items():
            self.items_listbox.insert(
                tk.END, f"{name}: {info['description']}, {info['contact']}")  # 将所有物品信息加入Listbox显示


if __name__ == "__main__":
    root = tk.Tk()
    app = ItemReviveApp(root)  # 实例化应用程序
    root.mainloop()  # 进入事件循环
