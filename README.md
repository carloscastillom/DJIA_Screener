# DJI_Screener
Stock market screener for the companies in the dow jones.

proven use of:
 1) Numpy - List
 2) Pandas - DataFrame
 3) yahoo_fin - 

## Dow Jones companies screener
This repository obtains the tickers of all companies in the dow jones index. It filters them based on the 52-week highest, lowest prices and the PE ratio of all the companies in the index. 

The exact conditions that the screener must fulfill are the following:

  1) Condition 1. Current price must be at lease 20% higher than the company's 52-week Low.
  2) Condition 2. Current price must be at most 10% lower than the company's 52-week high.
  3) Condition 3. PE-Ratio must be lower than 80.

The resulting Dataframe illustrates the companies of interest with the applied filters. 

Disclaimer: All investment strategies and investments involve risk of loss. Nothing contained in this website should be construed as investment advice.


