import numpy as np 

# 创建ndarray 的两种方式
# 第一种方式使用python列表创建一维数组
x = np.array([1,2,3])
print("一维数组: ", x)
# 如果是一维，整个数组相加
print(sum(x))

x = np.array([[1,2,3], [4,5,6]])
print("二维数组: \n", x)
#如果是二维, 列相加，返回一维ndarray 
print(sum(x))

# 如果参数中是可选的话，你得加key设置value
# x = np.random.randint(low=10, high=12, size=(3, 4))
x = np.random.randint(10, 12, size=(3, 4))
print("创建随机的一维数组: \n", x)
#创建二维数组
x = np.array([[1,2,3],[4,5,6]])
print("二维数组: \n", x)
print(type(x))
print("x.dtype = ", x.dtype)
print("x.shape = ",x.shape)

# 把ndarray 保存到文件
print("把ndarray 保存到文件x= \n",x)
np.save("wangweijun.txt", x)
print("从文件中读取ndarray ")
f = np.load("wangweijun.txt.npy")
print(f)


print("第二种方式numpy函数创建ndarray")

print("numpy函数创建3行4列元素全部为0的ndarray")
x = np.zeros(shape=(3,4), dtype='int32')

print(x)
print("元素数据类型: ",x.dtype)

x = np.full(shape=(4,5), fill_value=3)
print("np.full 函数创建ndarray: \n",x)

# 单位矩阵是主对角线上全是 1，其他位置全是 0 的方形矩阵
x = np.eye(5)
print("单位矩阵 :\n", x)

# 对角矩阵(仅在主对角线上有值的方形矩阵)
x = np.diag([10,20,30,40])
print("对角矩阵: \n",x)

x = np.diag([10,20,30,40], k=1)
print("对角矩阵 k=1: \n",x)

# 定区间内值均匀分布的 ndarray
x = np.arange(10)
print("定区间内值均匀分布的: \n", x)
x = np.arange(0, 10, 2)
print(x)
x = np.arange(start=0, stop=10, step=2)
print(x)

# axis=轴对称
x = np.linspace(2.0, 3.0, num=5)
print(x)

# axis=轴对称, 默认产生float，制定dtype
x = np.linspace(2, 20, num=5, dtype='int32')
print(x)

# 一维数组转二维数组
x = np.arange(9).reshape((3,3))
print(x)

# 创建随机的3行两列的ndarray, item 范围[0, 1]
x = np.random.rand(3,2)
print(x)
# 创建随机的3行两列的ndarray, item 范围[0, 10]
x = np.random.rand(3,2) * 10
print(x)

# 创建随机的3行3列的ndarray, item 范围[0, 10]
x = np.random.randint(high=10 ,low=0,  size=(3,3))
print(x)

# 随机生成指定均值与标准差的ndarray
x = np.random.normal(loc=0.0, scale=1.0, size=(4,4))
print(x)
#print(sum(x))
# 均值
print(x.mean())
print(x.shape)
# item 的数据类型
print(x.dtype)
print("x>0 个数为 ", (x>0).sum())
print("x<0 个数为 ", (x<0).sum())

x = np.random.randint(low=0,high=33, size=(4,4))
print(x)

# reshape 一维转二维, 创建连续二维数组
x = np.arange(start=2, stop=34, step=2).reshape(4,4)
print(x)
print(len(x))
# 元素个数
print(x.size)


x = np.linspace(2,32,16).reshape(4,4)
print(x)


#######################访问和删除 ndarray 中的元素及向其中插入元素##################
print("#######################访问和删除 ndarray 中的元素及向其中插入元素##################")
x = np.array([1, 2, 3, 4, 5])
print("origin ndarray :\n", x)
# 一维数组索引从正向
print(x[0])
# 索引从逆向
print(x[-1])

x[3] = 44444
print("modify ndarray :\n", x)

# 二维数组
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
# row, column的索引
print(x[2][1])

#########修改元素
x[2][1] = 99

print(x)

##########删除元素########
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])
leftArr = np.delete(x, [0,1], axis=0)
print("leftArr: \n", leftArr)
print(x)


# We create a rank 2 ndarray
y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y)
# 删除第0行与第2行 axis=0表示横轴
leftArr = np.delete(y, [0,2], axis=0)
print("删除第0行与第2行 leftArr: \n", leftArr)
print(y)

# 删除第0列与第2列 axis=1表示纵轴
leftArr = np.delete(y, [0,2], axis=1)
print("删除第0列与第2列 leftArr: \n", leftArr)
print(y)


############添加元素##############
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray 
y = np.array([[1,2,3],[4,5,6]])

# We print x
print()
print('Original x = ', x)

# append 添加到末尾
left = np.append(x, [6,7], axis=0)
print("一维数组添加之后 \n", left)
print(x)


left = np.append(y, [[7],[8]], axis=1)
print("二维数组添加(必须是维度一致)之后 \n", left)
print("原始的ndarray不会改变 y: \n" ,y)

############insert插入元素##############
left = np.insert(x, 0, [0, -1, -2], axis=0)
print("插入一维数组元素x: \n", left)
print(x)

left = np.insert(y, 0, [0,88], axis=1)
print("插入一列二维数组元素x: \n", left)
print(x)

left = np.insert(y, 0, [[0,88], [0,88]], axis=1)
print("插入二维数组元素x: \n", left)

# 插入的全部是0,只需要写一个
left = np.insert(y, 0, [0], axis=1)
print("插入二维数组元素x: \n", left)
print(x)


####################堆叠###########
# We create a rank 1 ndarray 
x = np.array([1,2])

# We create a rank 2 ndarray 
y = np.array([[3,4],[5,6]])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Y = \n', y)

#垂直堆叠tup 元组 We stack x on top of Y
result = np.vstack((x,y))
print("垂直堆叠stack x on top of Y : \n", result)
print("一维转二维 \n",x.reshape(2,1))
result = np.hstack((x.reshape(2,1),y))
print("横向堆叠 \n", result)

a = np.array([1, 2, 3]) 
b = np.array([2, 3, 4]) 
result = np.vstack((a,b)) 
print(result)









































