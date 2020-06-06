import pandas as pd #excel
import time #time
import numpy as np
from alpha_vantage.timeseries import TimeSeries

#open the file and get data as numpy array
file = 'stocks.xlsx' 
stocks = pd.read_excel(file)
#print(stocks)
stocks = stocks.to_numpy()
row,column = stocks.shape

#current allowed loss and required profit
loss = np.array(stocks[1:row,4])
buy = np.array(stocks[1:row,2]) #price at which bought
profit = np.array(stocks[1:row,3])

#array for current prices of the stocks
cur = np.array([])

#use alpha_vantage to find current price
api = 'ENTER_YOUR_API' #to get your API go to alphavantage website create a free account and copy paste the key between quotes
#example: api = 'ASDGWRIGVANVFBGB'
ts = TimeSeries(key=api, output_format='pandas')

i = 1
while i<row: #find current stock price of each stock in the list
    print(str(stocks[i,0]))
    data, meta_data = ts.get_intraday(symbol=str(stocks[i,0]), interval = '1min', outputsize = 'full')
    cur = np.append(cur,float(data.iat[0,3]))
    print(cur)
    i = i + 1
    time.sleep(12) #to ensure 5 calls per minute as max calls are 5 on AlphaVantage
    
#compare current prices with max allowed loss
i = 0
while i<row-1:
    if cur[i] < loss[i]:
        print("Take money out from" + str(stocks[i+1,1]))
        print('LOSS')
    elif cur[i] > profit[i]:
        print("Take money out from" + str(stocks[i+1,1]))
        print('PROFIT')
    else:
        print('')
        print('          Current Value of ' + str(stocks[i+1,1]) + ' is ' + str(cur[i]))
        calc = 100*(cur[i] - buy[i])/ buy[i]
        print('          Current Profit/loss ' + str(calc))
    i = i + 1
    
input("Press Enter to continue...")
