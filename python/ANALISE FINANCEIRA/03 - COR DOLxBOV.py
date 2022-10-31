from cProfile import label
from posixpath import split
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
import seaborn as sns

yf.pdr_override()
tickers = ['^BVSP', 'USDBRL=X']
carteira = web.get_data_yahoo(tickers, start="2007-01-01")["Close"]
carteira = carteira.dropna()
carteira.columns = ["DOLAR", "IBOV"]
print(carteira)

# carteira.plot(subplots=True, figsize=(22, 8))
# sns.set()
# sns.heatmap(carteira.corr(), annot=True)

carteira["IBOV_DOLARIZADO"] = (carteira["IBOV"] / carteira["DOLAR"])
sns.set()
carteira.plot(subplots=True, figsize=(22, 8))
plt.show()

# Quando a correlação está alta, significa que se um sobe, o outro sobe também.
carteira["DOLAR"].rolling(252).corr(carteira["IBOV"]).plot(figsize=(22,8))
sns.set()
plt.show()
