import numpy as np 

# 创建ndarray 的两种方式
# 第一种方式使用python列表创建一维数组
x = np.array([1,2,3])
print("一维数组: ", x)

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

# np.linspace








