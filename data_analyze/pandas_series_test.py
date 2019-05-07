import pandas as pd
import numpy as np

# 如何导入 Pandas
# 如何使用各种方法创建 Pandas Series 和 DataFrame
# 如何访问及更改 Series 和 DataFrame 中的元素
# 如何对 Series 执行算术运算
# 如何向 DataFrame 中加载数据
# 如何处理非数 (NaN) 值

# 为何要使用 Pandas
# 允许为行和列设定标签
# 可以针对时间序列数据计算滚动统计学指标
# 轻松地处理 NaN 值
# 能够将不同格式的数据加载到 DataFrame 中
# 可以将不同的数据集合并到一起
# 与 NumPy 和 Matplotlib 集成

groceries = pd.Series(data=[30, 6.0, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])

# x = np.array([1, 'asdf'])
# # ['1' 'asdf']
# print(x)
#
# x = np.array([1, 2.0])
# # [1. 2.]
# print(x)

# 第一列是索引，第二列是数据
print(groceries)
print(groceries.shape)
print("维度: ", groceries.ndim)
print("元素total: ", groceries.size)

print("data : ", groceries.values)
print("index: ", groceries.index)

# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# We check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

# We print the results
print()
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)

print()
# 单个索引
print("鸡蛋个数eggs :", groceries['eggs'])
print()
# 多个索引(name)
print(groceries[['eggs', 'apples']])
# we use loc to access multiple index labels
print()
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']])
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
# 多个索引(下标)
print('How many eggs and apples do we need to buy:\n', groceries[[0, 1]])
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]])
print()

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0])
print()

# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We change the number of eggs to 2
groceries['eggs'] = 2

# We display the changed grocery list
print()
print('Modified Grocery List:\n', groceries)

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples out of place:\n', groceries)

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace=True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples in place:\n', groceries)

print()
# We multiply our grocery list by 2
print(groceries * 2)