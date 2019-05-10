# We import Pandas as pd into Python
import pandas as pd


def print_data_frame():
    """
    打印data frame
    :return:
    """
    # We create a dictionary of Pandas Series
    items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
             'Alice': pd.Series(data=[40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}
    # We print the type of items to see that it is a dictionary
    print(type(items))
    print(items)
    # We create a Pandas DataFrame by passing it a dictionary of Pandas Series
    shopping_carts = pd.DataFrame(items)
    print()
    print(shopping_carts)
    # NaN 是指没有值(该行该列)
    # We print some information about shopping_carts
    print('shopping_carts has shape:', shopping_carts.shape)
    print('shopping_carts has dimension:', shopping_carts.ndim)
    print('shopping_carts has a total of:', shopping_carts.size, 'elements')
    print()
    print('The data in shopping_carts is:\n', shopping_carts.values)
    print()
    print('The row index in shopping_carts is:', shopping_carts.index)
    print()
    print('The column index in shopping_carts is:', shopping_carts.columns)


def print_no_index():
    """
    创建五索引的data frame
    :return:
    """
    # We create a dictionary of Pandas Series without indexes
    data = {'Bob': pd.Series([245, 25, 55]),
            'Alice': pd.Series([40, 110, 500, 45])}

    # We create a DataFrame
    df = pd.DataFrame(data)

    print()
    print(df)


def has_only_bob():
    # We create a dictionary of Pandas Series
    items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
             'Alice': pd.Series(data=[40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}
    # We Create a DataFrame that only has Bob's data
    bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

    # We display bob_shopping_cart
    print()
    print(bob_shopping_cart)

    # We Create a DataFrame that only has selected items for both Alice and Bob
    sel_shopping_cart = pd.DataFrame(items, index=['pants', 'book'])

    # We display sel_shopping_cart
    print()
    print("sel_shopping_cart: \n", sel_shopping_cart)

    # We Create a DataFrame that only has selected items for Alice
    alice_sel_shopping_cart = pd.DataFrame(items, index=['glasses', 'bike'], columns=['Alice'])

    # We display alice_sel_shopping_cart
    print()
    print(alice_sel_shopping_cart)


def no_index():
    data = {"Integers": [1, 2, 3], "floats": [1.1, 2.2, 3.3]}
    # 很像excel, 自动添加行索引
    df = pd.DataFrame(data)
    print("df:\n", df)


def add_index():
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)

    # We display the DataFrame
    print()
    print("store_items:\n", store_items)

    # 添加index的大小必须与items数组的size一致，否则报错
    store_items = pd.DataFrame(items2, index=['store1', 'store2'])

    print()
    print("store_items add index:\n", store_items)

    print()
    print("访问 Pandas DataFrame 中的元素")

    # 访问列,注意里面还有中括号
    print()
    print("访问列: \n", store_items[['bikes']])

    # 访问多列
    print()
    print("访问多列: \n", store_items[['bikes', 'glasses']])

    # 访问行
    print()
    print(store_items.loc[['store1']])

    # 访问多行
    print()
    print(store_items.loc[['store1', 'store2']])

    # 访问单个元素,注意先列后行

    print()
    print("访问单个元素,注意先列后行 \n", store_items['bikes']['store1'])

    # 修改data frame
    # 添加一列, 默认是添加到末尾
    store_items['shirts'] = [23, 89]
    print()
    print("添加shirts后: \n", store_items)

    store_items['suits'] = store_items['pants'] + store_items['shirts']

    print()
    print("添加suits(value 提供由pants， shirts)后: \n", store_items)


def insertColumn():
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)
    print(store_items)
    # 添加到指定某列之后
    store_items.insert(2, 'shopes', [3, 3])
    print("吧shopes插入glasses之后 \n", store_items)


# 添加一行
def add_new_row():
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)
    # We create a dictionary from a list of Python dictionaries that will number of items at the new store
    new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

    new_store = pd.DataFrame(data=new_items, index=['store3'])
    print("new_store : \n", new_store)

    store_items = store_items.append(new_store, sort=True)

    print('添加新店铺后: \n', store_items)


# print('store_items["shirts"] type : ', type(store_items['shirts']))
# print("store_items['shirts']) === \n", store_items['shirts'])
# print('store_items[["shirts"]] type : ', type(store_items[['shirts']]))
# print("store_items[['shirts']] === \n", store_items[['shirts']])
def add_new_watches_dataframe():
    """
    添加新列，从旧列中取值
     给店铺store2,store3 添加new_watches
    :return:
    """
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)
    store_items['new_watches'] = store_items['watches'][:2]
    print()
    print("给店铺store2,store3 添加new_watches: \n", store_items)


def pop_test():
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)
    print("original data : \n", store_items)
    store_items.pop('bikes')
    print("drop bikes : \n", store_items)


def drop_test():
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)
    print("original data : \n", store_items)
    # 单列
    # store_items = store_items.drop(columns=['bikes'])
    # store_items = store_items.drop(labels='bikes', axis=1)
    # 多列
    # store_items = store_items.drop(columns=['bikes', 'glasses'])
    # store_items = store_items.drop(labels=['bikes', 'glasses'], axis=1)

    # 删除行(根据行索引)
    # store_items.drop(index=0, inplace=True)
    store_items.drop(index=[0, 1], inplace=True)

    print("drop bikes : \n", store_items)


def rename_test():
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

    # We create a DataFrame
    store_items = pd.DataFrame(items2)
    print("original data : \n", store_items)

    # 修改列名
    # store_items.rename(columns={"bikes": "bikesssss", "glasses":"glassesssss"}, inplace=True)

    # 修改行名
    # store_items.rename({0: 10, 1: 11}, axis='index', inplace=True)
    store_items.rename(index={0: 10, 1: 11}, inplace=True)

    print("drop bikes : \n", store_items)

# print_data_frame()
# print_no_index()
# add_index()
# insertColumn()
# has_only_bob()
# add_new_row()
# no_index()
# add_new_watches_dataframe()
# pop_test()
# drop_test()
# rename_test()
