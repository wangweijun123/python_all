import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def read_csv():
    # 我们将 Google 股票数据加载到 DataFrame 中
    Google_stock = pd.read_csv('./google.csv')
    # 我们输出关于 Google_stock 的一些信息
    print('Google_stock is of type:', type(Google_stock))
    print('Google_stock has shape:', Google_stock.shape)
    # print(Google_stock)

    print("打印前5行")
    print(Google_stock.head())
    print("检查每列是否有null值")
    print(Google_stock.isnull().any())
    # We get descriptive statistics on our stock data
    print("DataFrame 每列的描述性统计信息")
    print(Google_stock.describe())
    print("DataFrame 这列的Adj Close统计信息")
    print(Google_stock['Adj Close'].describe())

    # We print information about our DataFrame
    print()
    print('Maximum values of each column:\n', Google_stock.max())
    print()
    print('Minimum Close value:', Google_stock['Close'].min())
    print()
    print('Average value of each column:\n', Google_stock.mean())

    # We display the correlation between columns
    print()
    print(Google_stock.corr())


def group_by_test():
    """
            Year	Name	Department	Age	Salary
        0	1990	Alice	HR	25	50000
        1	1990	Bob	RD	30	48000
        2	1990	Charlie	Admin	45	55000
        3	1991	Alice	HR	26	52000
        4	1991	Bob	RD	31	50000
        5	1991	Charlie	Admin	46	60000
        6	1992	Alice	Admin	27	60000
        7	1992	Bob	RD	32	52000
        8	1992	Charlie	Admin	28	62000

    :return:
    """
    data = pd.read_csv('./fake_company.csv')
    # We display the total amount of money spent in salaries each year
    data.groupby(['Year'])['Salary'].sum()
    # We display the average salary per year
    data.groupby(['Year'])['Salary'].mean()
    # We display the total salary each employee received in all the years they worked for the company
    data.groupby(['Name'])['Salary'].sum()
    # We display the salary distribution per department per year.
    data.groupby(['Year', 'Department'])['Salary'].sum()


def exercise():
    print()
    """
                     Date  Adj Close
        0  2004-08-19  49.845802
        1  2004-08-20  53.805050
        2  2004-08-23  54.346527
        3  2004-08-24  52.096165
        4  2004-08-25  52.657513
    """
    google_stock = pd.read_csv('./google.csv', usecols=['Date', 'Adj Close'], index_col=['Date'], parse_dates=['Date'])
    print('显示GOOGLE前5行数据')
    print(google_stock.head())
    # print(Google_stock[['Date', 'Adj Close']].head())
    # We load the Apple stock data into a DataFrame
    apple_stock = pd.read_csv('./AAPL.csv', usecols=['Date', 'Adj Close'], index_col=['Date'], parse_dates=['Date'])
    print('显示apple前5行数据')
    print(apple_stock.head())

    amazon_stock = pd.read_csv('./AMZN.csv', usecols=['Date', 'Adj Close'], index_col=['Date'], parse_dates=['Date'])
    print('显示amazon前5行数据')
    print(amazon_stock.head())

    # We create calendar dates between '2000-01-01' and  '2016-12-31'
    dates = pd.date_range('2000-01-01', '2016-12-31')

    # We create and empty DataFrame that uses the above dates as indices
    all_stocks = pd.DataFrame(index=dates)

    google_stock.rename(columns={'Adj Close': 'Google'}, inplace=True)
    print(google_stock.head())

    apple_stock.rename(columns={'Adj Close': 'Apple'}, inplace=True)
    print(apple_stock.head())

    amazon_stock.rename(columns={'Adj Close': 'Amazon'}, inplace=True)
    print(amazon_stock.head())

    # We join the Google stock to all_stocks
    all_stocks = all_stocks.join(google_stock)
    all_stocks = all_stocks.join(apple_stock)
    all_stocks = all_stocks.join(amazon_stock)
    print("打印  all_stocks")
    print(all_stocks.head())
    
    print(all_stocks.isnull().any())
    all_stocks.dropna(axis=0, inplace=True)
    print(all_stocks.head())
    print("平均值(指的是每一列的平均值):\n", all_stocks.mean())
    print('the average stock price for each stock')
    print(all_stocks.mean(axis=0), end='\n\n')
    print('the median stock price for each stock')
    print(all_stocks.median(axis=0), end='\n\n')
    print("标准差:\n", all_stocks.std())
    print("相关性:\n", all_stocks.corr())

    rollingMean = all_stocks['Google'].rolling(150).mean()
    print("隔 150 天的平均股价", rollingMean)



    # We plot the Google stock data
    plt.plot(all_stocks['Google'])

    # We plot the rolling mean ontop of our Google stock data
    plt.plot(rollingMean)
    plt.legend(['Google Stock Price', 'Rolling Mean'])
    plt.show()

# read_csv()
exercise()
