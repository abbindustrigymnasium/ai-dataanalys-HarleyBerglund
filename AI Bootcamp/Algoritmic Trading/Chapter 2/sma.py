import pandas as pd
from pandas_datareader import data
import statistics as stats
import matplotlib.pyplot as plt


start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'sma_stock_data.pkl'

try:
  stock_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
  stock_data2 = data.DataReader('TSLA', 'yahoo', start_date, end_date)
  stock_data2.to_pickle(SRC_DATA_FILENAME)

stock_data = stock_data2.tail(620)

close = stock_data['Close']


time_period = 20
history = []
sma_values = []
for close_price in close:
  history.append(close_price)
  if len(history) > time_period:
    del (history[0])

  sma_values.append(stats.mean(history))

stock_data = stock_data.assign(ClosePrice=pd.Series(close, index=stock_data.index))
stock_data = stock_data.assign(Simple20DayMovingAverage=pd.Series(sma_values, index=stock_data.index))

close_price = stock_data['ClosePrice']
sma = stock_data['Simple20DayMovingAverage']

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Stock price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
sma.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()