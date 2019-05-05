# -*- coding: cp936 -*-
import os

def rename_files():
    print("call rename method")
    # 第一步获取文件列表
    file_list = os.listdir(r"E:\study\udacity\python\entry_door\test")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"E:\study\udacity\python\entry_door\test")
    # 第二步 修改文件名
    for file_name in file_list:
        print("file_name:"+file_name)
        print(file_name.translate(None, "0123456"))
        os.rename(file_name, file_name.translate(None, "0123456"))


# 注意空格，python 的空格,方法的调用前面不能有空格
rename_files()
