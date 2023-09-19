import pandas as pd
import numpy as np
import pandas_datareader as pdr
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)

# print(pdr.__version__)
# sdf = pdr.get_data_yahoo('AAPL', start_date, end_date)
# sdf


import pandas_datareader.data as web
import yfinance as yf

yf.pdr_override()

# , end='2022-02-09' 005930.KS
data = web.get_data_yahoo('AAPL', start=start_date, end = end_date)
print(type(data), data)