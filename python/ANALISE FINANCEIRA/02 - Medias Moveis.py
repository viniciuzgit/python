from cProfile import label
from posixpath import split
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

import yfinance as yf
yf.pdr_override()

empresa = 'VALE3.SA'
ibov = web.get_data_yahoo(empresa)
# start='2010-05-03', end='2022-1-1'

ibov_fatiado = ibov[(ibov.index.year >= 2010) & (ibov.index.year <= 2022)]
print(ibov_fatiado["Close"].plot(figsize=(22,8), label="IBOV"))
print(ibov_fatiado["Close"].rolling(21).mean().plot(label="MM21"))
print(ibov_fatiado["Close"].rolling(200).mean().plot(label="MM200"))

plt.title(empresa)
plt.legend()
plt.show()