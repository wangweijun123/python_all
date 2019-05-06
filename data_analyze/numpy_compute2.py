import numpy as np

# 两个ndarray数组相加,减，乘，除, shape 必须一致
x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5, 7.5, 8.5])
print(x + y)

print(np.add(x, y))

print('x * y = ', x * y)
print('multiply(x,y) = ', np.multiply(x, y))
print()
print('x / y = ', x / y)
print('divide(x,y) = ', np.divide(x, y))

# x = 1
# y = 2
# print(np.add(x, y))


# We create two rank 2 ndarrays
X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([5.5, 6.5, 7.5, 8.5]).reshape(2, 2)
# We create two rank 2 ndarrays
X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([5.5, 6.5, 7.5, 8.5]).reshape(2, 2)

# We print X
print()
print('X = \n', X)

# We print Y
print()
print('Y = \n', Y)
print()

# We perform basic element-wise operations using arithmetic symbols and functions
print('X + Y = \n', X + Y)
print()
print('add(X,Y) = \n', np.add(X, Y))
print()
print('subtract(X,Y) = \n', np.subtract(X, Y))
print()
print('X * Y = \n', X * Y)
print()
print('multiply(X,Y) = \n', np.multiply(X, Y))
print()
print('X / Y = \n', X / Y)
print()
print('divide(X,Y) = \n', np.divide(X, Y))

# We create a rank 1 ndarray
# 对数组每一个元素进行开平方根
x = np.array([1, 2, 3, 4])
x = np.sqrt(x)
print(x)

x = np.array([[1, 2], [3, 4]])
# 求平均值
print(x.mean(axis=1))
# 求和(列)
print(x.sum(axis=0))
# 求和(row)
print(x.sum(axis=1))
# 标准差
print(x.std())
# 求平均值
print('Median of all elements in X:', np.median(X))
# 方法调用
print(x.max())
# 函数调用
print(np.max(x))

print(x + 3)

# 两个ndarray shape不一样的数组运算,
x = np.full(shape=(4, 4), fill_value=0)
print(x)

y = np.array([1, 2, 3, 4])
print(y)
# x[:, 1] = 2
# x[:, 2] = 3
# x[:, 3] = 4
# print(x)
print(x + y)
print()


# 对于不同形状的array nd，先扩展后计算

# We create a rank 1 ndarray
X = np.array([1, 2, 3])
# 扩展成
# [[1, 2, 3],
#  [1, 2, 3],
#  [1, 2, 3]]

# We create a 3 x 3 ndarray
Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# We create a 3 x 1 ndarray
Z = np.array([1, 2, 3]).reshape(3, 1)
# [[1]              [[1, 1, 1]
#  [2]   扩展成--->   [2, 2, 2]
#  [3]]                [3, 3, 3]]


# We print x
print()
print('X = ', X)
print()

# We print Y
print()
print('Y = \n', Y)
print()

# We print Z
print()
print('Z = \n', Z)
print()
# 更小的ndarray 扩展到更大的adarray数组再进行加减乘除运算
print("X+Y = \n", (X + Y))
print()
print('Z + Y = \n', Z + Y)


#
# print("X+Z = \n", (X+Z))

print()
print("X+Z = \n", (X+Z))

print()
print("X*Y = \n", (X*Y))


#  NumPy 并创建一个秩为 2 的 ndarray，其中包含 0 到 5,000（含）之间的随机整数，共有 1000 行和 20 列。


print()
X = np.random.randint(low=0, high=5000, size=(1000, 20))
print(X)
print(X.size)
print(X.shape)


