class Shirt:
    # self 是一个字典
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

class Shop:
    def __init__(self, size):
        self.size = size


# one_shirt = Shirt('red', 'large', 55)

# two_shirt = Shirt('bule', 'small', 10)

# print(one_shirt.price)
# one_shirt.change_price(99)
# print(one_shirt.price)

# shirs = []
# shirs.append(one_shirt)
# shirs.append(two_shirt)
# for item in shirs:
#     print(item)

# for index in range(len(shirs)):
#     print(index)

def test():
    print("called")