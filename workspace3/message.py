names = input("请输入名字列表...")
scores = input("请输入分数列表...")
print(names)
print(scores)

nameList = names.title().split(',')
scoreList = scores.title().split(',')
print(nameList)
print(scoreList)

for item in zip(nameList, scoreList):
    print(item)

# {} 花括号占位符
for name,score in zip(nameList, scoreList):
    print("姓名: {} 得分: {}".format(name, score))
    print(name + " " + score)