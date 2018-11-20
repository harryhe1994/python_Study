import pandas as pd

stock_change = pd.DataFrame([[10, 11, 12, 13, 14], [20, 21, 22, 23, 24]])
# print(pd.DataFrame(stock_change))

stock_code = ['股票' + str(i) for i in range(stock_change.shape[0])]
# print(stock_code)

date = pd.date_range('2017-01-01', periods=5, freq='B')
stock_change.columns = date
stock_change.index = stock_code
# data = pd.DataFrame(stock_change)
# print(stock_change)
print(stock_change)
# print(data.shape)
