import pandas as pd
from pandas_datareader import data
import statistics as stats
import matplotlib.pyplot as plt
import math as math


start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'stdev_stock_data.pkl'

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
stddev_values = []

for close_price in close:
  history.append(close_price)
  if len(history) > time_period: 
    del (history[0])

  sma = stats.mean(history)
  sma_values.append(sma)
  variance = 0
  for hist_price in history:
    variance = variance + ((hist_price - sma) ** 2)

  stdev = math.sqrt(variance / len(history))

  stddev_values.append(stdev)

stock_data = stock_data.assign(ClosePrice=pd.Series(close, index=stock_data.index))
stock_data = stock_data.assign(StandardDeviationOver20Days=pd.Series(stddev_values, index=stock_data.index))

close_price = stock_data['ClosePrice']
stddev = stock_data['StandardDeviationOver20Days']

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(211, ylabel='Google price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ax2 = fig.add_subplot(212, ylabel='Stddev in $')
stddev.plot(ax=ax2, color='b', lw=2., legend=True)
ax2.axhline(y=stats.mean(stddev_values), color='k')
plt.show()