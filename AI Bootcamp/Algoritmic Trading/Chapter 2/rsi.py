import pandas as pd
from pandas_datareader import data
import statistics as stats
import matplotlib.pyplot as plt


start_date = '2011-01-01'
end_date = '2021-04-14'
SRC_DATA_FILENAME = 'rsi_stock_data.pkl'

try:
    stock_data2 = pd.read_pickle(SRC_DATA_FILENAME)
except FileNotFoundError:
    stock_data2 = data.DataReader('CCIV', 'yahoo', start_date, end_date)
    stock_data2.to_pickle(SRC_DATA_FILENAME)

stock_data = stock_data2.tail(620)

close = stock_data['Close']

time_period = 20
gain_history = []
loss_history = []
avg_gain_values = []
avg_loss_values = []
rsi_values = []
last_price = 0

for close_price in close:
    if last_price == 0:
        last_price = close_price

    gain_history.append(max(0, close_price - last_price))
    loss_history.append(max(0, last_price - close_price))
    last_price = close_price

    if len(gain_history) > time_period:
        del (gain_history[0])
        del (loss_history[0])

    avg_gain = stats.mean(gain_history)
    avg_loss = stats.mean(loss_history)

    avg_gain_values.append(avg_gain)
    avg_loss_values.append(avg_loss)

    rs = 0
    if avg_loss > 0:
        rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))
    rsi_values.append(rsi)

stock_data = stock_data.assign(
    ClosePrice=pd.Series(close, index=stock_data.index))
stock_data = stock_data.assign(RelativeStrengthAvgGainOver20Days=pd.Series(
    avg_gain_values, index=stock_data.index))
stock_data = stock_data.assign(RelativeStrengthAvgLossOver20Days=pd.Series(
    avg_loss_values, index=stock_data.index))
stock_data = stock_data.assign(RelativeStrengthIndicatorOver20Days=pd.Series(
    rsi_values, index=stock_data.index))

close_price = stock_data['ClosePrice']
rs_gain = stock_data['RelativeStrengthAvgGainOver20Days']
rs_loss = stock_data['RelativeStrengthAvgLossOver20Days']
rsi = stock_data['RelativeStrengthIndicatorOver20Days']


fig = plt.figure()
ax1 = fig.add_subplot(311, ylabel='Stock price in $')
close_price.plot(ax=ax1, color='black', lw=2., legend=True)
ax2 = fig.add_subplot(312, ylabel='RS')
rs_gain.plot(ax=ax2, color='g', lw=2., legend=True)
rs_loss.plot(ax=ax2, color='r', lw=2., legend=True)
ax3 = fig.add_subplot(313, ylabel='RSI')
rsi.plot(ax=ax3, color='b', lw=2., legend=True)
plt.show()
