from turtle import title
from unicodedata import name
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# vamos pegar cotação do Indice e de Petrobras

#indice
df = web.DataReader(f'^BVSP', data_source='yahoo', start=f'01-29-2022', end='10-28-2022')
print(df)
df["Adj Close"].plot(figsize=(15, 10))
plt.show()

#PETR4
df = web.DataReader(f'PETR4.SA', data_source='yahoo', start=f'02-20-2020', end='02-20-2021')
print(df)
df["Adj Close"].plot(figsize=(15, 10))
plt.show()