# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 20:11:46 2018

@author: Matthew Dunahoe
"""

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2017, 4, 2)
end = dt.datetime(2018, 4, 2)
                  
prices = web.DataReader('GLW', 'iex', start, end)['close'] 

returns = prices.pct_change()

last_price = prices[-1]

#number of trials
num_simulations = 1000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count]*(1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
        
    simulation_df[x] = price_series
    
fig = plt.figure()
fig.suptitle('Monte Carlo Simultaion Corning, GLW')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('day')
plt.ylabel('Price')
plt.show()