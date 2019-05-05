mv_population = 6
mv_area = 2
# 执行完下面这句，mv_density值已经确定3
mv_density = mv_population/mv_area

#print(mv_density)

mv_population = 4
# mv_density 输出3
print(mv_density)

mv_density = mv_population/mv_area
print(mv_density)

x = int(4.7)
y = float(4)

print(x)
print(y)

print(type(x))
print(type(y))

# 因为 0.1 的浮点数（或近似值）实际上比 0.1 稍微大,所以false, 为何打印出来又是0.3
print(.1 + .1 + .1 == .3)
print(.1 + .1 + .1)
# 这个为什么为true
print(.1*10 == 1)

print(int(4.7))

#print(10/0)

age = 14
flag = age > 12 and age < 20
print(flag)

flag = age > 12 & age < 20
print(flag)

# 字符串与数字相乘  hellohellohellohellohello
word = "hello"
print(word*5)

print(word[0])

print(len(835))



