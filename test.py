from alpha_vantage.timeseries import TimeSeries

api = 'YOUR_API_KEY'
ts = TimeSeries(key=api, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='STOCK_SYMBOL/TICKER', interval = '1min', outputsize = 'full')
print(data)
