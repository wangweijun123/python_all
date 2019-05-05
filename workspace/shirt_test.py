import random
# from后面小写的shirt 指的是文件， import 大写的Shirt 是文件里面定义的class
from shirt import Shirt, Shop

one_shirt = Shirt('red', 'large', 55)
print(one_shirt.color)

shop = Shop(45)
print(shop.size)

random.randint()
# shirt.test()