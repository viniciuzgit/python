import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

import yfinance as yf
yf.pdr_override()

ibov = web.get_data_yahoo('^BVSP')
print(ibov.head())
print(ibov.tail())
print(ibov["Close"].plot(figsize=(22,8)))
plt.show()