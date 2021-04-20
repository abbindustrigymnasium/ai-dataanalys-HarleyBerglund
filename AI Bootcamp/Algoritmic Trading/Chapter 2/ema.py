import pandas as pd
from pandas_datareader import data
import statistics as stats
import matplotlib.pyplot as plt


start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'ema_stock_data.pkl'

try:
  stock_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
  stock_data2 = data.DataReader('TSLA', 'yahoo', start_date, end_date)
  stock_data2.to_pickle(SRC_DATA_FILENAME)

stock_data = stock_data2.tail(620)

close = stock_data['Close']

num_periods = 20
K = 2 / (num_periods + 1)
ema_p = 0

ema_values = []
for close_price in close:
  if (ema_p == 0):
    ema_p = close_price
  else:
    ema_p = (close_price - ema_p) * K + ema_p

  ema_values.append(ema_p)

stock_data = stock_data.assign(ClosePrice=pd.Series(close, index=stock_data.index))
stock_data = stock_data.assign(Exponential20DayMovingAverage=pd.Series(ema_values, index=stock_data.index))

close_price = stock_data['ClosePrice']
ema = stock_data['Exponential20DayMovingAverage']


fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Stock price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ema.plot(ax=ax1, color='b', lw=2., legend=True)
plt.show()