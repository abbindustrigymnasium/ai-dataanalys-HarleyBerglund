import pandas as pd
from pandas_datareader import data
import statistics as stats 
import matplotlib.pyplot as plt
import math as math


start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'bbands_stock_data.pkl'

try:
  stock_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
  stock_data2 = data.DataReader('TSLA', 'yahoo', start_date, end_date)
  stock_data2.to_pickle(SRC_DATA_FILENAME)

stock_data = stock_data2.tail(620)

close = stock_data['Close']

time_period = 20
stdev_factor = 2
history = []
sma_values = []
upper_band = []
lower_band = []

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

  upper_band.append(sma + stdev_factor * stdev)
  lower_band.append(sma - stdev_factor * stdev)

stock_data = stock_data.assign(ClosePrice=pd.Series(close, index=stock_data.index))
stock_data = stock_data.assign(MiddleBollingerBand20DaySMA=pd.Series(sma_values, index=stock_data.index))
stock_data = stock_data.assign(UpperBollingerBand20DaySMA2StdevFactor=pd.Series(upper_band, index=stock_data.index))
stock_data = stock_data.assign(LowerBollingerBand20DaySMA2StdevFactor=pd.Series(lower_band, index=stock_data.index))

close_price = stock_data['ClosePrice']
mband = stock_data['MiddleBollingerBand20DaySMA']
uband = stock_data['UpperBollingerBand20DaySMA2StdevFactor']
lband = stock_data['LowerBollingerBand20DaySMA2StdevFactor']

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Stock price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
mband.plot(ax=ax1, color='b', lw=2., legend=True)
uband.plot(ax=ax1, color='g', lw=2., legend=True)
lband.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()