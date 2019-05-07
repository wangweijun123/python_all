import numpy as np

x = np.arange(20)
w = x[4:10]
print("一唯数组 \n", w)

x = np.arange(20).reshape(4, 5)
print(x)
# 根据行索引与列索引访问某一个元素
print(x[3, 4])
# 获取ndarray子集
w = x[0:3, 2:4]
print("指定行与列的范围获取子集", w)

w = x[:3, 2:4]
print("简写取子集 \n", w)

# We select all the elements in the 3rd row, 返回一维数组
v = x[2, :]
# We print v
print()
print('第三行数据 v = \n', v)
print("根据索引取第三行数据 \n", x[2])

print("根据索引取第3列数据返回一维数组 \n", x[:, 3])

print("根据索引取第3列数据返回二维数组 \n", x[:, 3:4])

##############切片(根据行与列的范围进行索引)，数据不会复制到新的变量中,切片只是一个试图，如果改变试图，必然改变原始数据###########

x = np.arange(20).reshape(4, 5)
print(x)

y = x[1:3, 0:2]
print(y)
y[0][0] = 22
print("赋值后y二维数组被改变", y)
print("赋值后原始数组被改变", x)

##############copy切片,复制数据到新的ndarray中，与
x = np.arange(20).reshape(4, 5)
print(x)
xx = np.copy(x[1:3, 0:2])
xx[0][0] = 55
print(xx)
print("copy后操作新数组后与原数组无关，原数组不变", x)

# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1, 3])

# We print X
print()
print('X = \n', X)
print()

# We print indices
print('indices = ', indices)
print()

# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices, :]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]

# We print Y
print()
print('Y = \n', Y)

# We print Z
print()
print('Z = \n', Z)

#################获取对角线#############
x = np.arange(20).reshape(4, 5)
print(x)
print("对角线为 \n", np.diag(x))

###########获取ndarray中唯一元素，去重###########
# np.unique
# Create 3 x 3 ndarray with repeated values
X = np.array([[1, 2, 3], [5, 2, 8], [1, 2, 3]])

# We print X
print()
print('X = \n', X)
print()

# We print the unique elements of X 
print('The unique elements in X are:', np.unique(X))

###########布尔型索引、集合运算和排序##############

x = np.arange(25).reshape(5, 5)
print(x)

print("ndarray 数组中大于10的元素 \n", x[x > 10])

print("ndarray 数组中大于10小于20的元素，注意要小括号 \n", x[(x > 10) & (x < 20)])

x[(x > 10) & (x < 20)] = -1

print("大于10小于20的元素替换成-1 \n", x)

#########集合运算#######

# 查找两个ndarray相同的元素

x = np.array([1, 2, 3, 4, 5])
# We create a rank 1 ndarray
y = np.array([6, 7, 2, 8, 4])
print("相同元素 \n", np.intersect1d(x, y))
print('The elements that are in x that are not in y:', np.setdiff1d(x, y))
print('All the elements of x and y:', np.union1d(x, y))

x = np.random.randint(10, high=50, size=20)
print(x)
y = np.sort(x)
print(y)
print(x)

# sort 对一维数组排序和二维数组排序是一样的
x = np.random.randint(10, high=50, size=(3, 3))
print("original x \n", x)
# sort 当做函数调用时，不改变原来的数组
y = np.sort(x)
print(y)
print(x)
# 当做方法调用时，改变原数组
x.sort()
print(x)

# numpy  去重与排序
x = np.random.randint(1, 10, 20)
print(x)
y = np.unique(x)
print(y)
z = np.sort(y)
print(z)

# We create an unsorted rank 2 ndarray
X = np.random.randint(1, 11, size=(5, 5))

# We print X
print()
print('Original X = \n', X)
print()

# We sort the columns of X and print the sorted array
print()
print('X with sorted columns :\n', np.sort(X, axis=0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis=1))

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
x = np.arange(1, 26).reshape((5, 5))
# 從nd array 中尋找基数
y = x[x % 2 != 0]
print(y)
print(x)



# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1,3])

# We print X
print()
print('X = \n', X)
print()

# We print indices
print('indices = ', indices)
print()

# 指定某些行和某些列获取数据集
# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices,:]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]

# We print Y
print()
print('Y = \n', Y)

# We print Z
print()
print('Z = \n', Z)