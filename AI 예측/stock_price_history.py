import streamlit as st
import pandas_datareader as pdr
import pandas as pd

st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다!
''')

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
df = pd.read_csv('005930.KS_5y.csv')
st.line_chart(df.Close)
st.line_chart(df.Volume)