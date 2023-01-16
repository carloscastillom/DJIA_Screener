# DJIA_Screener
Stock market screener for the companies in the Dow Jones Industrial Average. the information Contained can be changed fairly easy, you can modify the filters as you wish.


may reuse this for the project.

proven use of:
 1) Numpy - use of Lists.
 2) Pandas -use of DataFrame.
 3) yahoo_fin - library that obtains information out of yahoo finance.

## Dow Jones Industrial Average Companies Screener
This repository obtains the tickers of all companies in the Dow Jones Industrial Average. T It filters them based on the 52-week highest, lowest prices and the PE ratio of all the companies in the index. 

The exact conditions that the screener must fulfill are the following:

  1) Condition 1. Current price must be at lease 20% higher than the company's 52-week Low.
  2) Condition 2. Current price must be at most 10% lower than the company's 52-week high.
  3) Condition 3. PE-Ratio must be lower than 80.

The resulting Dataframe, runned in January 2022, shows two companies of interest based on the applied filters. 

 - Visa (V)

 ![Visa](https://user-images.githubusercontent.com/65776444/158386041-8116cd47-1b5a-4112-b1bd-bf3313745463.png)

The company is cyclical which means it moves as the US and Global economy does. It is in the dominant player in the credit card market in US. 

Paste the growth of earnings. compare with Master card and other players

 
 - Home Depot (HD)

 ![HomeDepot](https://user-images.githubusercontent.com/65776444/158386944-de2d8da0-d0a0-470f-b6e2-f31fffb8d748.png)

Its a stong player in the home improvement market in the US. The company offers different kinds of building materials and Home Improvement articles

Paste the growth of earnings. compare with Master card and other players.

competitors. Lowes, Menards


Disclaimer: All investment strategies and investments involve risk of loss. Nothing contained in this website should be construed as investment advice.


