

"""
读取一行
"""
def testReadLine():
    file = open('E:/study/udacity/python/workspace3/my_file2.txt', 'r')
    data = file.readline() # 读取一行 wangweijunaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbb
    #fiel.readline(2) # 读取两个字符 wa
    print(data)
    file.close()



"""
每次读取指定大小的字符长度
"""
def testReadSize():
    file2 = open('E:/study/udacity/python/workspace3/my_file2.txt', 'r')
    print(file2.read(4))  # 读取两个字符 wang
    print(file2.read(3))  # 读取两个字符 wei
    print(file2.read(3))  # 读取两个字符 jun
    print(file2.readline()) # aaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbb
    file2.close()


#每次读取一行文本内容
#wangweijunaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbb
#the second line
#third line
def testReadLineEveryTime():
    file3 = open('E:/study/udacity/python/workspace3/my_file2.txt', 'r')
    print(file3.readline()) # wangweijunaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbb
    print(file3.readline()) # the second line
    print(file3.readline()) # third line
    print(file3.readline()) # 
    msg = file3.readline() # 
    print(msg)

    print('msg =="" is ' + str(msg == "")) # 判断字符串为空字符串的话，使用  msg ==""
    if msg is None:
        print('msg == None')
    else:
        print('msg == None is false')
    file3.close()

"""
使用while循环读取文件内容,存入列表中
"""
def testUseWhileReadLine():
    file4 = open('E:/study/udacity/python/workspace3/my_file2.txt', 'r')
    content = []
    while True:
        line = file4.readline()
        if (line != ""):
            print(line)
            content.append(line.strip()) # 去掉换行符
        else:
            print("结束了")
            break
    file4.close()
    print(content)


"""
 使用while循环读取文件文本内容，存入list
"""
def testReadLineSave2List():
    file5 = open('E:/study/udacity/python/workspace3/my_file2.txt', 'r')
    content = []
    while True:
        line = file5.readline()
        if (line != ""):
            print(line)
            content.append(line.strip()) # 去掉换行符
        else:
            print("结束了")
            break
    file5.close()
    print(content)


"""
with open file 使用for循环遍历
"""
def testWithOpenFile():
    with open('E:/study/udacity/python/workspace3/my_file2.txt', 'r') as f:
        content = []
        for line in f:
            content.append(line.strip())
        print(content)



def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            array = line.split(',')
            print(array)
            print("len = " + str(len(array))) # 列表的长度 len
            if len(array) > 0:
                print(array[0])
                cast_list.append(array[0])
    print(cast_list)
    for actor in cast_list:
        print(actor)






testReadLine()
testReadSize()
testReadLineEveryTime()
testUseWhileReadLine()
testReadLineSave2List()
testWithOpenFile()
create_cast_list('E:/study/udacity/python/workspace3/flying_circus_cast.txt')