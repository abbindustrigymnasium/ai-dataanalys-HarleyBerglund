import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data

start_date = '2014-01-01'
end_date = '2021-01-01'
SRC_DATA_FILENAME = 'macd_stock_data.pkl'

try:
  stock_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
  stock_data2 = data.DataReader('TSLA', 'yahoo', start_date, end_date)
  stock_data2.to_pickle(SRC_DATA_FILENAME)

stock_data = stock_data2.tail(620)

close = stock_data['Close']

num_periods_fast = 10
K_fast = 2 / (num_periods_fast + 1)
ema_fast = 0
num_periods_slow = 40
K_slow = 2 / (num_periods_slow + 1)
ema_slow = 0
num_periods_macd = 20
K_macd = 2 / (num_periods_macd + 1)
ema_macd = 0

ema_fast_values = []
ema_slow_values = []
macd_values = []
macd_signal_values = []
macd_historgram_values = []
for close_price in close:
  if (ema_fast == 0):
    ema_fast = close_price
    ema_slow = close_price
  else:
    ema_fast = (close_price - ema_fast) * K_fast + ema_fast
    ema_slow = (close_price - ema_slow) * K_slow + ema_slow

  ema_fast_values.append(ema_fast)
  ema_slow_values.append(ema_slow)

  macd = ema_fast - ema_slow
  if ema_macd == 0:
    ema_macd = macd
  else:
    ema_macd = (macd - ema_macd) * K_macd + ema_macd

  macd_values.append(macd)
  macd_signal_values.append(ema_macd)
  macd_historgram_values.append(macd - ema_macd)

stock_data = stock_data.assign(ClosePrice=pd.Series(close, index=stock_data.index))
stock_data = stock_data.assign(FastExponential10DayMovingAverage=pd.Series(ema_fast_values, index=stock_data.index))
stock_data = stock_data.assign(SlowExponential40DayMovingAverage=pd.Series(ema_slow_values, index=stock_data.index))
stock_data = stock_data.assign(MovingAverageConvergenceDivergence=pd.Series(macd_values, index=stock_data.index))
stock_data = stock_data.assign(Exponential20DayMovingAverageOfMACD=pd.Series(macd_signal_values, index=stock_data.index))
stock_data = stock_data.assign(MACDHistorgram=pd.Series(macd_historgram_values, index=stock_data.index))

close_price = stock_data['ClosePrice']
ema_f = stock_data['FastExponential10DayMovingAverage']
ema_s = stock_data['SlowExponential40DayMovingAverage']
macd = stock_data['MovingAverageConvergenceDivergence']
ema_macd = stock_data['Exponential20DayMovingAverageOfMACD']
macd_histogram = stock_data['MACDHistorgram']


fig = plt.figure()
ax1 = fig.add_subplot(311, ylabel='Stock price in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
ema_f.plot(ax=ax1, color='b', lw=2., legend=True)
ema_s.plot(ax=ax1, color='r', lw=2., legend=True)
ax2 = fig.add_subplot(312, ylabel='MACD')
macd.plot(ax=ax2, color='black', lw=2., legend=True)
ema_macd.plot(ax=ax2, color='g', lw=2., legend=True)
ax3 = fig.add_subplot(313, ylabel='MACD')
macd_histogram.plot(ax=ax3, color='r', kind='bar', legend=True, use_index=False)
plt.show()