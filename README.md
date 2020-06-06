# Investment
Python script that uses AlphaVantage to gather information about specified stocks and keeps a track on the profit/loss.

In Excel file:
Do not change the name of the file. Input the following data:
Ticker: Stock Symbol. For NASDAQ stocks, Enter only the symbol, for other stocks enter the market with the symbol. eg: for Starbucks (NASDAQ) input SBUX, for FedEx NYSE:FDX
Stocks: input name of the stock.
Buying price: input the price at which stock was bought.
Selling price: input the price at which you would like to sell the stock.
Loss: input the minimum price at which you will sell the stock in case of loss.

In python script:
Use alpha vantage to get a api key for free by making an account. Copy the API key at the right location.

In test file:
(in case the script is crashing/not working for over 1 minute)
(this occurs when some of the stock data is incorrect)
change the api with your API
change the symbol value to the stock ticker you have entered in excel one by one.
the stock ticker for which no information is recieved/error is recieved needs to be amended.

Modules: pip install these
alpha_vantage
numpy
pandas

tested on Python 3.6

this script can also be automated to run whenever the computer gets connected to the internet. (tested)
