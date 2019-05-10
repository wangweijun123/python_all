import pandas as pd
import numpy as np


def handle_nan():
    """
    查找nan值，个数
    :return:
    """
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes': 8, 'suits': 45},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5, 'shirts': 2, 'shoes': 5, 'suits': 7},
              {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes': 10}]

    # We create a DataFrame  and provide the row index
    store_items = pd.DataFrame(items2, index=['store 1', 'store 2', 'store 3'])

    # We display the DataFrame
    print(store_items)
    # We count the number of NaN values in store_items
    x = store_items.isnull().sum().sum()
    # We print x
    print('Number of NaN values in our DataFrame:', x)

    # We print the number of non-NaN values in our DataFrame
    print()
    print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())
    print()
    print(store_items.isnull().any())


def delete_row_column_nan():
    """
    查找nan值，个数
    :return:
    """
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes': 8, 'suits': 45},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5, 'shirts': 2, 'shoes': 5, 'suits': 7},
              {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes': 10}]

    store_items = pd.DataFrame(items2, index=['store 1', 'store 2', 'store 3'])
    print(store_items)

    # {0 or 'index', 1 or 'columns'},
    # store_items.dropna(axis=0, inplace=True)
    store_items.dropna(axis=1, inplace=True)
    print(store_items)


def replace_nan():
    """
    查找nan值，个数
    :return:
    """
    print()
    # We create a list of Python dictionaries
    items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes': 8, 'suits': 45},
              {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5, 'shirts': 2, 'shoes': 5, 'suits': 7},
              {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes': 10}]

    store_items = pd.DataFrame(items2, index=['store 1', 'store 2', 'store 3'])
    print("原始数据 :\n", store_items)

    # store_items.fillna(0, inplace=True)
    # store_items.fillna(method='ffill', inplace=True)
    store_items.fillna(method='backfill', inplace=True)

    print()
    print("修改后 :\n", store_items)


def test():
    pd.set_option('precision', 1)
    books = pd.Series(
        data=['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland'])
    authors = pd.Series(
        data=['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll'])

    user_1 = pd.Series(data=[3.2, np.nan, 2.5])
    user_2 = pd.Series(data=[5., 1.3, 4.0, 3.8])
    user_3 = pd.Series(data=[2.0, 2.3, np.nan, 4])
    user_4 = pd.Series(data=[4, 3.5, 4, 5, 4.2])

    dat = {'Book Title': books, "authors": authors, "user_1": user_1, "user_2": user_2, "user_3": user_3,
           "user_4": user_4}

    book_ratings = pd.DataFrame(data=dat)

    print(book_ratings)
    print()
    print(book_ratings.mean())
    print(type(book_ratings.mean()))
    # 使用列平均值替换nan
    book_ratings.fillna(book_ratings.mean(), inplace=True)
    print()
    print("替换null值 \n", book_ratings)

    best_rated = book_ratings[(book_ratings == 5).any(axis=1)]['Book Title'].values
    print(best_rated)


handle_nan()
# delete_row_column_nan()
# replace_nan()
# test()
