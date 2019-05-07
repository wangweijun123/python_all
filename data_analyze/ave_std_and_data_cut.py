import numpy as np
# 迷你项目
#  NumPy 并创建一个秩为 2 的 ndarray，其中包含 0 到 5,000（含）之间的随机整数，共有 1000 行和 20 列。


print()
X = np.random.randint(low=0, high=5000, size=(1000, 20))
print(X)
print(X.size)
print(X.shape)

# Average of the values in each column of X
ave_cols = np.average(X, axis=0)
print("每一列的平均值 \n", ave_cols)
# ave_cols2 = np.mean(X, axis=0)
# # print("每一列的平均值 \n", ave_cols2)
print(len(ave_cols))
print(ave_cols.shape)

# 每一行的平均值
# ave_cols = np.average(X, axis=1)
# print(len(ave_cols))


std_cols = np.std(X, axis=0)
print("每一列的标准差 \n", std_cols)
#print(len(std_cols))
print(std_cols.shape)

# Mean normalize X
X_norm = (X - ave_cols) / std_cols
print("均值标准化 ： \n", X_norm)
print(X_norm.shape)



# Print the average of all the values of X_norm
print("𝑋  平均值: ", np.average(X_norm))
print("𝑋  平均值: ", X_norm.mean())

# Print the minimum value of each column of X_norm
min_columns = np.min(X_norm, axis=0)
print("每一列的最小值", min_columns)
print(min_columns.shape)

# Print the maximum value of each column of X_norm
max_columns = np.max(X_norm, axis=0)
print("每一列的最大值", max_columns)
print(max_columns.shape)

# We create a random permutation of integers 0 to 4
print(np.random.permutation(5))
# shape格式为 (rows,columns)
print(X_norm.shape)

X_norm_row_num = X_norm.shape[0]
print("数据集, 一共有行数为:", X_norm_row_num)
row_indices = np.random.permutation(X_norm_row_num)
print("行的随机索引列表", row_indices)
print(row_indices.shape)

# Create a Training Set
first_end = np.int(X_norm_row_num*0.6)

X_train = X_norm[row_indices[0:first_end], :]
print("训练集 : \n", first_end, X_train.shape)

# Create a Cross Validation Set
second_end = np.int(X_norm_row_num*0.8)
X_crossVal = X_norm[row_indices[first_end:second_end], :]
print("交叉验证集 : \n", second_end, X_crossVal.shape)

# Create a Test Set
X_test = X_norm[row_indices[second_end:], :]
print("测试集 \n", X_test.shape)