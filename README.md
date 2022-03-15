# DJI_Screener
Stock market screener for the companies in the Dow Jones Industrial Average

proven use of:
 1) Numpy - use of Lists.
 2) Pandas -use of DataFrame.
 3) yahoo_fin - library that obtains information out of yahoo finance.

## Dow Jones companies screener
This repository obtains the tickers of all companies in the Dow Jones Industrial Average. T It filters them based on the 52-week highest, lowest prices and the PE ratio of all the companies in the index. 

The exact conditions that the screener must fulfill are the following:

  1) Condition 1. Current price must be at lease 20% higher than the company's 52-week Low.
  2) Condition 2. Current price must be at most 10% lower than the company's 52-week high.
  3) Condition 3. PE-Ratio must be lower than 80.

The resulting Dataframe illustrates the companies of interest based on the applied filters. 

 - Visa (V)

 ![Visa](https://user-images.githubusercontent.com/65776444/158386041-8116cd47-1b5a-4112-b1bd-bf3313745463.png)
 
 - Home Depot (HD)





Disclaimer: All investment strategies and investments involve risk of loss. Nothing contained in this website should be construed as investment advice.


