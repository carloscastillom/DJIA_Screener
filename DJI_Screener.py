import pandas as pd
from pandas.core.frame import DataFrame
import pandas_datareader as web 
import yfinance as yf
from yahoo_fin import stock_info as si
import time
import datetime as dt

tickers = si.tickers_dow() 
print(tickers)

tickershort=tickers[:4]

#start and end time 
start = dt.datetime.now() - dt.timedelta(days=365)
end = dt.datetime.now()


data=[]

for ticker in tickers:

    #data frame of prices information
    df = web.DataReader(ticker, 'yahoo', start, end)

    #list of required information
    listInfoTicker=[]

    #calculate the required information - they will be a column in a datafram
    latest_price = round(df['Adj Close'][-1],2)
    pe_ratio = si.get_quote_table(ticker)['PE Ratio (TTM)']
    low_52_week = round(min(df['Low'][-(52*5):]),2)
    high_52_week = round(max(df['High'][-(52*5):]),2)

    #add the required information in a list by ticker
    listInfoTicker.extend([ticker,latest_price,pe_ratio,low_52_week,high_52_week])
    
    #========conditions========
    #condition 1
    condition_1 = latest_price >= (1.2*low_52_week)
    #condition 2
    condition_2 = latest_price <= (0.9*high_52_week)
    #condition 3
    condition_3 = pe_ratio <=80
    
    if (condition_1) and (condition_2) and (condition_3):
        #add the information to the list of lists
        data.append(listInfoTicker)
    print(data)

DJI_stocks=pd.DataFrame(data, columns=['Ticker', 'Latest-Price', 'PE-Ratio', '52-week-Low', '52-week-high'])
DJI_stocks= DJI_stocks.sort_values(by=['PE-Ratio'])
print(DJI_stocks)
    #print(testSI)



