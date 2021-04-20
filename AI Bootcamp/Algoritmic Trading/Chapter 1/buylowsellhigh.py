from pandas_datareader import data
start_date = '2011-01-01'
end_date = '2021-01-01'
stock_data = data.DataReader('NIO', 'yahoo', start_date, end_date)


import numpy as np
import pandas as pd

stock_data_signal = pd.DataFrame(index=stock_data.index)
stock_data_signal['price'] = stock_data['Adj Close']
stock_data_signal['daily_difference'] = stock_data_signal['price'].diff()
stock_data_signal['signal'] = 0.0
stock_data_signal['signal'][:] = np.where(stock_data_signal['daily_difference'][:] > 0, 1.0, 0.0)

stock_data_signal['positions'] = stock_data_signal['signal'].diff()

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Stock price in $')
stock_data_signal['price'].plot(ax=ax1, color='r', lw=2.)

ax1.plot(stock_data_signal.loc[stock_data_signal.positions == 1.0].index,
         stock_data_signal.price[stock_data_signal.positions == 1.0],
         '^', markersize=5, color='m')

ax1.plot(stock_data_signal.loc[stock_data_signal.positions == -1.0].index,
         stock_data_signal.price[stock_data_signal.positions == -1.0],
         'v', markersize=5, color='k')

#plt.show()


# Set the initial capital
initial_capital= float(1000.0)

positions = pd.DataFrame(index=stock_data_signal.index).fillna(0.0)
portfolio = pd.DataFrame(index=stock_data_signal.index).fillna(0.0)


positions['TSLA'] = stock_data_signal['signal']
portfolio['positions'] = (positions.multiply(stock_data_signal['price'], axis=0))
portfolio['cash'] = initial_capital - (positions.diff().multiply(stock_data_signal['price'], axis=0)).cumsum()
portfolio['total'] = portfolio['positions'] + portfolio['cash']
portfolio.plot()
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')
portfolio['total'].plot(ax=ax1, lw=2.)
ax1.plot(portfolio.loc[stock_data_signal.positions == 1.0].index,portfolio.total[stock_data_signal.positions == 1.0],'^', markersize=10, color='m')
ax1.plot(portfolio.loc[stock_data_signal.positions == -1.0].index,portfolio.total[stock_data_signal.positions == -1.0],'v', markersize=10, color='k')
plt.show()