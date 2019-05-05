# 路劲注意是正斜线
f = None
try:
    f = open('E:/study/udacity/python/workspace3/my_file.txt', 'r')
    # 读取文件
    file_data = f.read()
    # f.write('adbc') # exception
    print(file_data)
except:
    print("error")
finally:
    print(f)
    if f != None: #  等价于  f is not None
        print('close')
        f.close()

# 删除行 ctrl+shift+k

# 写文件(之前文件中内容被覆盖)
ff = open('E:/study/udacity/python/workspace3/my_file.txt', 'w')
ff.write('wangweijun')
ff.close()

# 向文件中追加添文本
fff = open('E:/study/udacity/python/workspace3/my_file.txt', 'a')
fff.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
fff.close()

# with : 使用完文件后自动关闭文件句柄
print('with : 使用完文件后自动关闭stream')
with open('E:/study/udacity/python/workspace3/my_file.txt', 'r') as ffff:
    file_Data = ffff.read()
    print(file_Data)


with open('E:/study/udacity/python/workspace3/my_file.txt', 'a') as file1:
    file1.write('bbbbbbbbb')


