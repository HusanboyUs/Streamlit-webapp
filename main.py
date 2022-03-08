import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen
from datetime import date


#to get today's date
today=date.today()

#titles and subtitles
st.title('Crypto Currency Analyser App')
st.header('Used Technologies: Python, Streamlit(Data fetching and presenting)')
st.subheader('Khusanjon Usmonov ID-55119.code')

#here I am assiging variables for getting info in yfiance
Bitcoin='BTC-USD'
Eithereum='ETH-USD'
Ripple='XRP-USD'
BitcoinCash='BCH-USD'

#Access data from Yahoo Finance
BTC_Data=yf.Ticker(Bitcoin)
ETH_Data=yf.Ticker(Eithereum)
XRP_Data=yf.Ticker(Ripple)
BCH_Data=yf.Ticker(BitcoinCash)

#fetch the data history from Yahoo
BTHHis=BTC_Data.history(period='max')
ETHHis=BTC_Data.history(period='max')
XRPHis=BTC_Data.history(period='max')
BCHHis=BTC_Data.history(period='max')

#fetch crypto data for data frame
BTC=yf.download(Bitcoin, start=today, end=today)
ETH=yf.download(Eithereum, start=today, end=today)
XRP=yf.download(Ripple, start=today, end=today)
BCH=yf.download(BitcoinCash, start=today, end=today)


#Rendering data of Bitcoin to the template
st.write('BITCOIN ($)')
imageBTC=Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
#display data frame
st.table(BTC)
#Display a chart
st.bar_chart(BTHHis.Close)

#Rendering data of Bitcoin to the template
st.write('Eithereum ($)')
imageBTC=Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageBTC)
#display data frame
st.table(ETH)
#Display a chart
st.bar_chart(BTHHis.Close)

#Rendering data of Bitcoin to the template
st.write('Ripple ($)')
imageBTC=Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageBTC)
#display data frame
st.table(XRP)
#Display a chart
st.bar_chart(BTHHis.Close)

#Rendering data of Bitcoin to the template
st.write('BitcoinCash ($)')
imageBTC=Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBTC)
#display data frame
st.table(BCH)
#Display a chart
st.bar_chart(BTHHis.Close)